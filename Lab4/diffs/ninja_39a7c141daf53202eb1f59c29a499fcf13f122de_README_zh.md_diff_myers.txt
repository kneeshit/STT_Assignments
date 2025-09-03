diff --git a/README_zh.md b/README_zh.md
index 74384ee..5e8a895 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -86,7 +86,7 @@ opkg install luci-i18n-opengpt-zh-cn_1.0.6-1_all.ipk
 ```shell
 docker run --rm -it -p 7999:7999 --name=opengpt \
   -e OPENGPT_WORKERS=1 \
-  -e OPENGPT_LOG_LEVEL=info \
+  -e OPENGPT_LOG=info \
   gngpp/opengpt:latest serve run
 ```
 
@@ -102,7 +102,7 @@ services:
     restart: unless-stopped
     environment:
       - TZ=Asia/Shanghai
-      - OPENGPT_PROXIES=socks5://cloudflare-warp:10000
+      - OPENGPT_PROXIES=socks5://warp:10000
       # - OPENGPT_CONFIG=/serve.toml
       # - OPENGPT_PORT=8080
       # - OPENGPT_HOST=0.0.0.0
@@ -115,11 +115,11 @@ services:
     ports:
       - "8080:7999"
     depends_on:
-      - cloudflare-warp
+      - warp
 
-  cloudflare-warp:
-    container_name: cloudflare-warp
-    image: ghcr.io/gngpp/cloudflare-warp:latest
+  warp:
+    container_name: warp
+    image: ghcr.io/gngpp/warp:latest
     restart: unless-stopped
 
   watchtower:
@@ -157,7 +157,7 @@ services:
 - 可接入IP代理池，提高并发
 
 - 参数说明
-  - `--level`，环境变量 `OPENGPT_LOG_LEVEL`，日志级别: 默认info
+  - `--level`，环境变量 `OPENGPT_LOG`，日志级别: 默认info
   - `--host`，环境变量 `OPENGPT_HOST`， 服务监听地址: 默认0.0.0.0，
   - `--port`，环境变量 `OPENGPT_PORT`， 监听端口: 默认7999
   - `--tls-cert`，环境变量 `OPENGPT_TLS_CERT`，TLS证书公钥，支持格式: EC/PKCS8/RSA
@@ -179,7 +179,7 @@ Options:
   -H, --host <HOST>
           Server Listen host [env: OPENGPT_HOST=] [default: 0.0.0.0]
   -L, --level <LEVEL>
-          Log level (info/debug/warn/trace/error) [env: OPENGPT_LOG_LEVEL=] [default: info]
+          Log level (info/debug/warn/trace/error) [env: OPENGPT_LOG=] [default: info]
   -P, --port <PORT>
           Server Listen port [env: OPENGPT_PORT=] [default: 7999]
   -W, --workers <WORKERS>
