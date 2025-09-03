diff --git a/README.md b/README.md
index 17e98b7..2d46efb 100644
--- a/README.md
+++ b/README.md
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
@@ -158,7 +158,7 @@ services:
 - API documentation
 
 - Parameter Description
-  - `--level`, environment variable `OPENGPT_LOG_LEVEL`, log level: default info
+  - `--level`, environment variable `OPENGPT_LOG`, log level: default info
   - `--host`, environment variable `OPENGPT_HOST`, service listening address: default 0.0.0.0,
   - `--port`, environment variable `OPENGPT_PORT`, listening port: default 7999
   - `--tls-cert`, environment variable `OPENGPT_TLS_CERT`', TLS certificate public key. Supported format: EC/PKCS8/RSA
@@ -180,7 +180,7 @@ Options:
   -H, --host <HOST>
           Server Listen host [env: OPENGPT_HOST=] [default: 0.0.0.0]
   -L, --level <LEVEL>
-          Log level (info/debug/warn/trace/error) [env: OPENGPT_LOG_LEVEL=] [default: info]
+          Log level (info/debug/warn/trace/error) [env: OPENGPT_LOG=] [default: info]
   -P, --port <PORT>
           Server Listen port [env: OPENGPT_PORT=] [default: 7999]
   -W, --workers <WORKERS>
