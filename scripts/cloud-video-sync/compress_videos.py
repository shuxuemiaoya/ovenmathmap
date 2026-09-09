#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
微课视频轻量无损批量压缩工具
专为板书/PPT 类教学微课优化：
- 支持多进程并发压制
- 自动利用 macOS VideoToolbox 硬件加速或高质量 libx264
- 支持单视频试运行测试 (--test)
- 保持相对目录结构，支持断点续跑
"""

import os
import sys
import json
import shutil
import subprocess
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed

def check_ffmpeg() -> str:
    ffmpeg_path = shutil.which("ffmpeg")
    if not ffmpeg_path:
        # 尝试常见 Homebrew 路径
        for p in ["/opt/homebrew/bin/ffmpeg", "/usr/local/bin/ffmpeg"]:
            if os.path.exists(p):
                return p
        print("❌ 未检测到 ffmpeg，请先运行命令安装：brew install ffmpeg")
        sys.exit(1)
    return ffmpeg_path

def probe_hardware_encoder(ffmpeg_bin: str) -> str:
    try:
        res = subprocess.run([ffmpeg_bin, "-encoders"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "h264_videotoolbox" in res.stdout:
            return "h264_videotoolbox"
    except Exception:
        pass
    return "libx264"

def compress_single_video(ffmpeg_bin: str, src_path: str, dst_path: str, encoder: str) -> dict:
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    
    src_size = os.path.getsize(src_path)
    if os.path.exists(dst_path) and os.path.getsize(dst_path) > 1024 * 10:
        return {
            "status": "skipped",
            "src": src_path,
            "dst": dst_path,
            "src_size": src_size,
            "dst_size": os.path.getsize(dst_path)
        }

    tmp_dst = dst_path + ".tmp.mp4"
    if os.path.exists(tmp_dst):
        os.remove(tmp_dst)

    # 针对板书教学视频优化参数：
    # - 视频码率约 700kbps-800kbps（板书静态为主，极度清晰且体积仅原视频 1/4）
    # - 音频 64kbps AAC（人声微课足够清晰）
    # - -movflags +faststart：将 moov atom 移到文件头部，支持网页/CDN 秒开播放，无需缓冲整段视频
    if encoder == "h264_videotoolbox":
        cmd = [
            ffmpeg_bin, "-y", "-i", src_path,
            "-c:v", "h264_videotoolbox", "-b:v", "750k",
            "-c:a", "aac", "-b:a", "64k",
            "-movflags", "+faststart",
            tmp_dst
        ]
    else:
        cmd = [
            ffmpeg_bin, "-y", "-i", src_path,
            "-c:v", "libx264", "-crf", "26", "-preset", "faster",
            "-c:a", "aac", "-b:a", "64k",
            "-movflags", "+faststart",
            tmp_dst
        ]

    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if proc.returncode != 0:
            if os.path.exists(tmp_dst):
                os.remove(tmp_dst)
            return {"status": "error", "src": src_path, "error": proc.stderr[-300:]}
        
        os.rename(tmp_dst, dst_path)
        dst_size = os.path.getsize(dst_path)
        return {
            "status": "success",
            "src": src_path,
            "dst": dst_path,
            "src_size": src_size,
            "dst_size": dst_size,
            "ratio": (1 - dst_size / src_size) * 100 if src_size > 0 else 0
        }
    except Exception as e:
        if os.path.exists(tmp_dst):
            os.remove(tmp_dst)
        return {"status": "error", "src": src_path, "error": str(e)}

def find_all_videos(source_dir: str):
    video_files = []
    for root, _, files in os.walk(source_dir):
        for f in files:
            if f.endswith(".mp4") and not f.startswith("."):
                video_files.append(os.path.join(root, f))
    return sorted(video_files)

def main():
    parser = argparse.ArgumentParser(description="微课视频轻量无损压制工具")
    parser.add_argument("--config", default="config.json", help="配置文件路径")
    parser.add_argument("--test", action="store_true", help="仅测试压缩 1 个视频以验证画质与压缩比")
    parser.add_argument("--workers", type=int, default=4, help="并发压制进程数（默认4）")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, args.config)
    
    src_dir = "/Users/oven/Downloads/中小学智慧平台资源/习题库"
    dst_dir = "/Users/oven/Downloads/中小学智慧平台资源/习题库_compressed"
    
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)
            src_dir = cfg.get("source_dir", src_dir)
            dst_dir = cfg.get("compressed_dir", dst_dir)

    ffmpeg_bin = check_ffmpeg()
    encoder = probe_hardware_encoder(ffmpeg_bin)
    print(f"🎬 已就绪 ffmpeg: {ffmpeg_bin}")
    print(f"⚡ 选用编码器: {encoder} ({'Apple Silicon 硬件加速' if encoder == 'h264_videotoolbox' else 'CPU 软件编码'})")
    print(f"📂 源目录: {src_dir}")
    print(f"💾 输出目录: {dst_dir}")

    all_videos = find_all_videos(src_dir)
    total_count = len(all_videos)
    print(f"📊 发现共 {total_count} 个视频文件")

    if total_count == 0:
        print("⚠️ 未找到任何待处理的 MP4 视频。")
        return

    if args.test:
        test_video = all_videos[0]
        rel_path = os.path.relpath(test_video, src_dir)
        target_video = os.path.join(dst_dir, rel_path)
        print(f"\n🧪 [测试模式] 正在压制单个示例视频: {rel_path}")
        res = compress_single_video(ffmpeg_bin, test_video, target_video, encoder)
        if res["status"] == "success":
            print(f"✅ 压制测试成功！")
            print(f"   原始大小: {res['src_size'] / (1024*1024):.2f} MB")
            print(f"   压缩后大小: {res['dst_size'] / (1024*1024):.2f} MB")
            print(f"   瘦身体积: 缩减了 {res['ratio']:.1f}%")
            print(f"   测试文件保存于: {target_video}")
            print("\n👉 您可以在 Finder 中打开该视频查看画质与播放效果。确认满意后可直接运行全量压制。")
        else:
            print(f"❌ 测试失败: {res}")
        return

    print(f"🚀 开始全量批量压制 (并发数: {args.workers})...\n")
    processed = 0
    saved_bytes = 0
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = {}
        for src in all_videos:
            rel = os.path.relpath(src, src_dir)
            dst = os.path.join(dst_dir, rel)
            fut = pool.submit(compress_single_video, ffmpeg_bin, src, dst, encoder)
            futures[fut] = rel

        for fut in as_completed(futures):
            processed += 1
            rel = futures[fut]
            res = fut.result()
            if res["status"] == "success":
                saved = res["src_size"] - res["dst_size"]
                saved_bytes += saved
                print(f"[{processed}/{total_count}] ✅ {rel} ({res['src_size']/(1024*1024):.1f}MB -> {res['dst_size']/(1024*1024):.1f}MB, 瘦身 {res['ratio']:.0f}%)")
            elif res["status"] == "skipped":
                print(f"[{processed}/{total_count}] ⏩ 跳过已存在: {rel}")
            else:
                print(f"[{processed}/{total_count}] ❌ 失败: {rel} | 错误: {res.get('error')}")

    print(f"\n🎉 压制任务完成！累计为您节省硬盘与云端流量空间: {saved_bytes / (1024**3):.2f} GB！")

if __name__ == "__main__":
    main()
