diff --git a/README.md b/README.md
index d8e3ba3..f9e333d 100644
--- a/README.md
+++ b/README.md
@@ -66,6 +66,54 @@ docker run --rm -it -p 7999:7999 --hostname=opengpt \
   gngpp/opengpt:latest serve run
 ```
 
+> docker-compose
+
+```yaml
+version: '3'
+
+services:
+  opengpt:
+    image: ghcr.io/gngpp/opengpt:latest
+    container_name: opengpt
+    restart: unless-stopped
+    environment:
+      - TZ=Asia/Shanghai
+      - OPENGPT_CONFIG=/opengpt-serve.toml
+      # - OPENGPT_PORT=8080
+      # - OPENGPT_HOST=0.0.0.0
+      # - OPENGPT_WORKERS=10
+      # - OPENGPT_PROXY=
+      # - OPENGPT_TIMEOUT=360
+      # - OPENGPT_CONNECT_TIMEOUT=60
+      # - OPENGPT_TCP_KEEPALIVE=60
+      # - OPENGPT_TLS_CERT=
+      # - OPENGPT_TLS_KEY=
+      # - OPENGPT_UI_API_PREFIX=
+      # - OPENGPT_SIGNATURE=
+      # - OPENGPT_TB_ENABLE=
+      # - OPENGPT_TB_STORE_STRATEGY
+      # - OPENGPT_TB_REDIS_URL=
+      # - OPENGPT_TB_CAPACITY=
+      # - OPENGPT_TB_FILL_RATE=
+      # - OPENGPT_TB_EXPIRED=
+      # - OPENGPT_CF_SITE_KEY=
+      # - OPENGPT_CF_SECRET_KEY=
+    volumes:
+    #   - ${PWD}/ssl:/etc
+      - ${PWD}/opengpt-serve.toml:/opengpt-serve.toml
+    command: serve run
+    ports:
+      - "7999:7999"
+
+  watchtower:
+    container_name: watchtower
+    image: containrrr/watchtower
+    volumes:
+      - /var/run/docker.sock:/var/run/docker.sock
+    command: --interval 3600 --cleanup
+    restart: unless-stopped
+```
+
 > #### OpenWrt
 
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
@@ -139,6 +187,12 @@ Options:
           Token bucket fill rate [env: OPENGPT_TB_FILL_RATE=] [default: 1]
       --tb-expired <TB_EXPIRED>
           Token bucket expired (second) [env: OPENGPT_TB_EXPIRED=] [default: 86400]
+      --cf-site-key <CF_SITE_KEY>
+          Cloudflare turnstile captcha site key [env: OPENGPT_CF_SITE_KEY=]
+      --cf-secret-key <CF_SECRET_KEY>
+          Cloudflare turnstile captcha secret key [env: OPENGPT_CF_SECRET_KEY=]
+  -D, --disable-webui
+          Disable WebUI [env: OPENGPT_DISABLE_WEBUI=]
   -h, --help
           Print help
 ```
