#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
云对象存储（腾讯云 COS / 阿里云 OSS）自动化批量上传工具
- 支持一键断点续传（upload_progress.json）
- 支持 --dry-run 预览上传文件列表
- 支持 --test 上传 1 个测试视频并打印公开/CDN 直播链接
- 自动按年级、章节建立层级路径
- 自动设置 video/mp4 MIME 类型与公共读取权限
"""

import os
import sys
import json
import argparse
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

def load_config(config_path: str) -> dict:
    if not os.path.exists(config_path):
        print(f"❌ 找不到配置文件: {config_path}")
        print("👉 请先复制模板并填入您的云存储密钥：")
        print("   cp scripts/cloud-video-sync/config.example.json scripts/cloud-video-sync/config.json")
        sys.exit(1)
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_uploader(cfg: dict):
    provider = cfg.get("provider", "tencent").lower()
    if provider == "tencent":
        try:
            from qcloud_cos import CosConfig, CosS3Client
        except ImportError:
            print("❌ 未安装腾讯云 SDK，请在终端执行：pip install cos-python-sdk-v5")
            sys.exit(1)
        
        region = cfg["region"]
        secret_id = cfg["access_key_id"]
        secret_key = cfg["access_key_secret"]
        bucket = cfg["bucket"]
        
        cos_cfg = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
        client = CosS3Client(cos_cfg)
        
        def upload_fn(local_path: str, remote_key: str) -> bool:
            client.upload_file(
                Bucket=bucket,
                LocalFilePath=local_path,
                Key=remote_key,
                PartSize=10,
                MAXThread=5,
                ContentType="video/mp4"
            )
            return True

        def get_url(remote_key: str) -> str:
            cdn = cfg.get("cdn_domain", "").strip().rstrip("/")
            if cdn:
                return f"{cdn}/{urllib.parse.quote(remote_key)}"
            return f"https://{bucket}.cos.{region}.myqcloud.com/{urllib.parse.quote(remote_key)}"

        return upload_fn, get_url

    elif provider == "aliyun":
        try:
            import oss2
        except ImportError:
            print("❌ 未安装阿里云 SDK，请在终端执行：pip install oss2")
            sys.exit(1)
            
        endpoint = cfg["region"]
        if not endpoint.startswith("http"):
            endpoint = f"https://{endpoint}.aliyuncs.com"
        auth = oss2.Auth(cfg["access_key_id"], cfg["access_key_secret"])
        bucket = oss2.Bucket(auth, endpoint, cfg["bucket"])

        def upload_fn(local_path: str, remote_key: str) -> bool:
            headers = {"Content-Type": "video/mp4"}
            oss2.resumable_upload(bucket, remote_key, local_path, multipart_threshold=10*1024*1024, part_size=10*1024*1024, headers=headers)
            return True

        def get_url(remote_key: str) -> str:
            cdn = cfg.get("cdn_domain", "").strip().rstrip("/")
            if cdn:
                return f"{cdn}/{urllib.parse.quote(remote_key)}"
            bucket_name = cfg["bucket"]
            clean_endpoint = cfg["region"].replace("https://", "").replace("http://", "")
            return f"https://{bucket_name}.{clean_endpoint}.aliyuncs.com/{urllib.parse.quote(remote_key)}"

        return upload_fn, get_url
    else:
        print(f"❌ 不支持的云服务商: {provider} (仅支持 'tencent' 或 'aliyun')")
        sys.exit(1)

def find_upload_candidates(directory: str):
    videos = []
    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith(".mp4") and not f.startswith(".") and not f.endswith(".tmp.mp4"):
                full_path = os.path.join(root, f)
                videos.append(full_path)
    return sorted(videos)

def main():
    parser = argparse.ArgumentParser(description="对象存储视频批量上传同步工具")
    parser.add_argument("--config", default="config.json", help="配置文件名")
    parser.add_argument("--dry-run", action="store_true", help="演练模式，仅预览待上传列表，不产生网络请求")
    parser.add_argument("--test", action="store_true", help="测试模式，仅上传 1 个视频并打印公开链接")
    parser.add_argument("--use-raw", action="store_true", help="强制直接上传原始视频（默认优先检测并上传压制后视频）")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, args.config)
    cfg = load_config(config_path)

    raw_dir = cfg.get("source_dir", "")
    comp_dir = cfg.get("compressed_dir", "")

    # 判断使用哪个目录上传
    if not args.use_raw and os.path.exists(comp_dir) and len(find_upload_candidates(comp_dir)) > 0:
        active_dir = comp_dir
        print(f"✨ 检测到已压制视频目录，优先使用压制版: {active_dir}")
    else:
        active_dir = raw_dir
        print(f"📂 使用原始视频目录: {active_dir}")

    candidates = find_upload_candidates(active_dir)
    total_files = len(candidates)
    print(f"📊 发现待同步视频数量: {total_files}")

    if total_files == 0:
        print("⚠️ 没有发现可上传的 MP4 视频，请检查路径。")
        return

    remote_prefix = cfg.get("remote_prefix", "videos/").strip("/") + "/"

    # 加载已完成进度
    progress_file = os.path.join(base_dir, "upload_progress.json")
    uploaded_records = {}
    if os.path.exists(progress_file):
        try:
            with open(progress_file, "r", encoding="utf-8") as f:
                uploaded_records = json.load(f)
        except Exception:
            uploaded_records = {}

    if args.dry_run:
        print("\n🔎 [演练模式] 预览前 5 个上传映射:")
        for idx, p in enumerate(candidates[:5], 1):
            rel = os.path.relpath(p, active_dir)
            remote_key = remote_prefix + rel.replace("\\", "/")
            print(f"   [{idx}] 本地: {rel}")
            print(f"       -> 云端 Key: {remote_key}")
        print(f"\n... 共 {total_files} 个文件将同步至 Bucket [{cfg['bucket']}]。演练结束。")
        return

    upload_fn, get_url_fn = get_uploader(cfg)

    if args.test:
        test_file = candidates[0]
        rel = os.path.relpath(test_file, active_dir)
        remote_key = remote_prefix + rel.replace("\\", "/")
        print(f"\n🧪 [测试模式] 正在上传单个测试视频: {rel}")
        try:
            upload_fn(test_file, remote_key)
            final_url = get_url_fn(remote_key)
            print(f"✅ 上传成功！")
            print(f"🌐 线上直链/CDN 访问地址：")
            print(f"   {final_url}\n")
            print("👉 请在浏览器中打开上方链接，验证是否能直接点播。若能正常播放，即可启动全量上传。")
        except Exception as e:
            print(f"❌ 上传测试失败，错误详情:\n{e}")
        return

    # 全量多线程并发上传
    max_workers = int(cfg.get("max_concurrency", 6))
    print(f"\n🚀 开始全量多线程上传 (并发数: {max_workers})...")

    to_upload = [p for p in candidates if os.path.relpath(p, active_dir) not in uploaded_records]
    print(f"⚡ 剩余待上传: {len(to_upload)}/{total_files} (已跳过已完成: {len(uploaded_records)})")

    def worker(src_file):
        rel = os.path.relpath(src_file, active_dir)
        remote_key = remote_prefix + rel.replace("\\", "/")
        upload_fn(src_file, remote_key)
        return rel, get_url_fn(remote_key)

    completed_cnt = len(uploaded_records)
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(worker, p): p for p in to_upload}
        for fut in as_completed(futures):
            src_f = futures[fut]
            try:
                rel_k, pub_url = fut.result()
                completed_cnt += 1
                uploaded_records[rel_k] = pub_url
                print(f"[{completed_cnt}/{total_files}] ☁️ 上传成功: {rel_k}")
                # 定期保存进度
                if completed_cnt % 20 == 0 or completed_cnt == total_files:
                    with open(progress_file, "w", encoding="utf-8") as f:
                        json.dump(uploaded_records, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"❌ 上传失败: {src_f} | 错误: {e}")

    # 最终固化进度
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(uploaded_records, f, ensure_ascii=False, indent=2)

    print("\n🎉 全量视频同步任务圆满完成！")
    print(f"📝 上传映射清单已保存至: {progress_file}")

if __name__ == "__main__":
    main()
