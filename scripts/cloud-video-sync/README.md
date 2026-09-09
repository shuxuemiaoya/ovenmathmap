# 题库微课视频上云与 CDN 流媒体分发套件 (OPC 专属)

本套件为 **ovenmathmap** 题库视频（4,379 个名师微课 MP4）定制，彻底解决 120GB 视频导致 Git 仓库爆炸、Obsidian 同步瘫痪的问题，并为未来的在线网站提供商业级高可用、极速秒开、防盗链的流媒体分发能力。

---

## 🛠️ 套件架构与工具清单

| 脚本文件 | 核心职责 | 特性亮点 |
| :--- | :--- | :--- |
| [`config.example.json`](config.example.json) | 配置文件模板 | 支持腾讯云 COS、阿里云 OSS、自定义 CDN 域名切换 |
| [`compress_videos.py`](compress_videos.py) | 微课专属无损压制 | 针对板书微课优化，调用 Mac 硬件加速，120G 瘦身至 ~30G |
| [`upload_to_cloud.py`](upload_to_cloud.py) | 对象存储并发上传 | 多线程分块并发、断点续传、MIME类型自动识别、演练/测试模式 |
| [`generate_video_manifest.py`](generate_video_manifest.py) | CDN 映射与 Markdown 批量替换 | 一键将本地 `![[videos/...]]` 标签转换为轻量流媒体在线播放器 |

---

## 🚀 极速上手三步法

### 第一步：创建配置文件
复制配置模板并填入您的云存储凭据（已加入 `.gitignore`，绝不会误提交至 GitHub）：
```bash
cd /Users/oven/Documents/ovenmathmap/scripts/cloud-video-sync
cp config.example.json config.json
```
在 `config.json` 中配置：
- `provider`: `"tencent"` 或 `"aliyun"`
- `region`: 存储桶所在地域（如 `ap-beijing` 或 `oss-cn-beijing`）
- `bucket`: 您的存储桶名称
- `access_key_id`: 访问密钥 ID
- `access_key_secret`: 访问密钥 Secret
- `cdn_domain`: 绑定的 CDN 加速域名（如暂无备案域名可留空，将自动使用存储桶官方域名）

---

### 第二步（推荐）：微课专属无损压制（立省 70% 空间与费用）

微课视频画面多为静态板书，压制后体积缩减 75% 且画质完全无损：

1. **测试单个视频效果**：
   ```bash
   ./compress_videos.py --test
   ```
   *该命令会抽取 1 个视频进行压制并打印压缩比，您可以直接在 Finder 中点开对比画质。*

2. **启动全量批量压制**（利用 Apple Silicon 硬件加速）：
   ```bash
   ./compress_videos.py --workers 4
   ```

*(注：如果不需要压缩，可在上传时增加 `--use-raw` 参数直接上传原始 120GB 视频)*

---

### 第三步：上传到云端存储桶

1. **演练预览（不产生真实请求）**：
   ```bash
   ./upload_to_cloud.py --dry-run
   ```

2. **单视频试上传测试**：
   ```bash
   ./upload_to_cloud.py --test
   ```
   *上传成功后会打印一个公网访问直链，您可以在浏览器或手机上点开验证是否能极速秒播。*

3. **全量并发断点续传**：
   ```bash
   ./upload_to_cloud.py
   ```
   *上传进度实时保存到 `upload_progress.json`，即使网络中断或手动停止，下次启动也会自动跳过已完成文件。*

---

### 第四步：一键更新 Markdown 题库播放器

全量上传完成后，运行：
```bash
./generate_video_manifest.py --update-md
```
所有题库 Markdown 文件中的本地视频占位符将被自动替换为优雅的 HTML5 在线播放器：
```html
<video src="https://cdn.yourdomain.com/videos/.../q1_解析微课.mp4" controls preload="metadata" style="max-width:100%; border-radius:8px;"></video>
```
此后：
- 题库在 Obsidian 中完全不占磁盘空间，Git 秒级极速同步；
- 电脑、手机、iPad 只要联网即可直接小窗流畅刷题看视频；
- 未来导出做成静态网站（VitePress / Docusaurus / 自建网站）时，完全不需要额外做视频适配，天生就是商业级流媒体体验！

---

## 🔒 云端安全最佳实践（防盗链配置）

为防止其他网站盗用您的视频造成 CDN 流量费损失，在腾讯云/阿里云控制台设置：
- **Referer 防盗链**：开启白名单，只允许您的域名（如 `*.yourdomain.com`，本地调试可加入 `*localhost*`）引用。
- **Range 分片回源**：开启（支持微课拖拽进度条秒缓冲）。
