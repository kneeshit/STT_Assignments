diff --git a/README_zh.md b/README_zh.md
index ee53e7a..4825ae1 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -78,7 +78,7 @@ services:
     restart: unless-stopped
     environment:
       - TZ=Asia/Shanghai
-      - OPENGPT_PROXY=socks5://cloudflare-warp:40000
+      - OPENGPT_PROXY=socks5://cloudflare-warp:10000
       # - OPENGPT_CONFIG=/opengpt-serve.toml
       # - OPENGPT_PORT=8080
       # - OPENGPT_HOST=0.0.0.0
@@ -109,7 +109,6 @@ services:
 
   cloudflare-warp:
     container_name: cloudflare-warp
-    hostname: cloudflare
     image: ghcr.io/gngpp/cloudflare-warp:latest
     restart: unless-stopped
 
