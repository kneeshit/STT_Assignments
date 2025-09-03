diff --git a/README.md b/README.md
index f9e333d..fff238f 100644
--- a/README.md
+++ b/README.md
@@ -78,11 +78,11 @@ services:
     restart: unless-stopped
     environment:
       - TZ=Asia/Shanghai
-      - OPENGPT_CONFIG=/opengpt-serve.toml
+      - OPENGPT_PROXY=socks5://cloudflare-warp:40000
+      # - OPENGPT_CONFIG=/opengpt-serve.toml
       # - OPENGPT_PORT=8080
       # - OPENGPT_HOST=0.0.0.0
       # - OPENGPT_WORKERS=10
-      # - OPENGPT_PROXY=
       # - OPENGPT_TIMEOUT=360
       # - OPENGPT_CONNECT_TIMEOUT=60
       # - OPENGPT_TCP_KEEPALIVE=60
@@ -103,7 +103,15 @@ services:
       - ${PWD}/opengpt-serve.toml:/opengpt-serve.toml
     command: serve run
     ports:
-      - "7999:7999"
+      - "8080:7999"
+    depends_on:
+      - cloudflare-warp
+
+  cloudflare-warp:
+    container_name: cloudflare-warp
+    hostname: cloudflare
+    image: ghcr.io/gngpp/cloudflare-warp:latest
+    restart: unless-stopped
 
   watchtower:
     container_name: watchtower
