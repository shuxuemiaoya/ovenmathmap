#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
视频 CDN 映射表生成与 Markdown 播放器替换工具
1. 提取所有题库视频的线上 CDN 直播链接，生成全局字典 video_cdn_manifest.json
2. 提供一键替换 Markdown 题库视频引用的功能：
   将原本占用同步的本地内嵌：
     > ![[videos/q1_解析微课.mp4]]
   平滑转换为零体积占用的在线 HTML5 流媒体播放器：
     <video src="https://cdn.domain.com/videos/.../q1_解析微课.mp4" controls preload="metadata" width="100%"></video>
"""

import os
import sys
import json
import re
import argparse
import urllib.parse

def load_config(config_path: str) -> dict:
    if not os.path.exists(config_path):
        print(f"❌ 找不到配置文件: {config_path}")
        sys.exit(1)
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_cdn_url(cfg: dict, rel_video_path: str) -> str:
    cdn = cfg.get("cdn_domain", "").strip().rstrip("/")
    remote_prefix = cfg.get("remote_prefix", "videos/").strip("/") + "/"
    clean_rel = rel_video_path.replace("\\", "/").lstrip("/")
    full_key = remote_prefix + clean_rel
    
    if cdn:
        return f"{cdn}/{urllib.parse.quote(full_key)}"
    
    provider = cfg.get("provider", "tencent").lower()
    bucket = cfg["bucket"]
    region = cfg["region"]
    if provider == "tencent":
        return f"https://{bucket}.cos.{region}.myqcloud.com/{urllib.parse.quote(full_key)}"
    else:
        clean_endpoint = region.replace("https://", "").replace("http://", "")
        return f"https://{bucket}.{clean_endpoint}.aliyuncs.com/{urllib.parse.quote(full_key)}"

def scan_and_generate_manifest(cfg: dict, source_dir: str, output_manifest_path: str):
    manifest = {}
    total_found = 0

    for root, _, files in os.walk(source_dir):
        for f in files:
            if f.endswith(".mp4") and not f.startswith(".") and not f.endswith(".tmp.mp4"):
                full_p = os.path.join(root, f)
                rel_p = os.path.relpath(full_p, source_dir)
                cdn_url = build_cdn_url(cfg, rel_p)
                manifest[rel_p] = {
                    "cdn_url": cdn_url,
                    "filename": f,
                    "local_path": full_p
                }
                total_found += 1

    with open(output_manifest_path, "w", encoding="utf-8") as out_f:
        json.dump(manifest, out_f, ensure_ascii=False, indent=2)

    print(f"✅ 已成功扫描并生成视频 CDN 映射表: {output_manifest_path}")
    print(f"📊 映射视频总数: {total_found} 条")
    return manifest

def update_markdown_files(source_dir: str, manifest: dict, dry_run: bool = False):
    print(f"\n🔄 正在扫描并更新 Markdown 文件中的视频标签 (模式: {'演练预览' if dry_run else '实际修改'})...")
    md_updated = 0
    tags_replaced = 0

    # 匹配 ![[videos/xxx.mp4]]
    pattern = re.compile(r'>\s*!\[\[(?:videos/)?([^\]]+\.mp4)\]\]', re.IGNORECASE)

    for root, _, files in os.walk(source_dir):
        for f in files:
            if f.endswith(".md"):
                md_path = os.path.join(root, f)
                with open(md_path, "r", encoding="utf-8") as rf:
                    content = rf.read()

                if "videos/" not in content and ".mp4" not in content:
                    continue

                parent_rel = os.path.relpath(root, source_dir)

                def replacer(match):
                    nonlocal tags_replaced
                    video_name = match.group(1).split("/")[-1]
                    # 匹配 manifest 中的对应路径
                    matched_url = ""
                    for rel_k, info in manifest.items():
                        if info["filename"] == video_name and parent_rel in rel_k:
                            matched_url = info["cdn_url"]
                            break
                    if not matched_url:
                        # 降级尝试全局匹配文件名
                        for rel_k, info in manifest.items():
                            if info["filename"] == video_name:
                                matched_url = info["cdn_url"]
                                break

                    if matched_url:
                        tags_replaced += 1
                        return f'> <video src="{matched_url}" controls preload="metadata" style="max-width:100%; border-radius:8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></video>'
                    return match.group(0)

                new_content = pattern.sub(replacer, content)

                if new_content != content:
                    md_updated += 1
                    if not dry_run:
                        with open(md_path, "w", encoding="utf-8") as wf:
                            wf.write(new_content)
                    print(f"   ✍️ {'[预览]' if dry_run else '[已更新]'} {os.path.relpath(md_path, source_dir)}")

    print(f"\n🎉 处理完毕！共替换 {tags_replaced} 处微课视频标签，涉及 {md_updated} 篇 Markdown 文件。")

def main():
    parser = argparse.ArgumentParser(description="视频 CDN 映射与 Markdown 播放器替换工具")
    parser.add_argument("--config", default="config.json", help="配置文件名")
    parser.add_argument("--manifest", default="video_cdn_manifest.json", help="输出清单文件名")
    parser.add_argument("--update-md", action="store_true", help="自动替换 Markdown 文件中的本地视频标签为在线流媒体播放器")
    parser.add_argument("--dry-run", action="store_true", help="仅预览替换效果，不修改原文件")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, args.config)
    cfg = load_config(config_path)

    manifest_path = os.path.join(base_dir, args.manifest)
    src_dir = cfg.get("source_dir", "/Users/oven/Downloads/中小学智慧平台资源/习题库")

    manifest = scan_and_generate_manifest(cfg, src_dir, manifest_path)

    if args.update_md:
        update_markdown_files(src_dir, manifest, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
