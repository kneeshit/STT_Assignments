diff --git a/README.md b/README.md
index b6dd546..32c4357 100644
--- a/README.md
+++ b/README.md
@@ -78,7 +78,7 @@ services:
     environment:
       - TZ=Asia/Shanghai
       - OPENGPT_PROXY=socks5://cloudflare-warp:10000
-      # - OPENGPT_CONFIG=/opengpt-serve.toml
+      # - OPENGPT_CONFIG=/serve.toml
       # - OPENGPT_PORT=8080
       # - OPENGPT_HOST=0.0.0.0
       # - OPENGPT_WORKERS=10
@@ -99,7 +99,7 @@ services:
       # - OPENGPT_CF_SECRET_KEY=
     volumes:
       # - ${PWD}/ssl:/etc
-      - ${PWD}/opengpt-serve.toml:/opengpt-serve.toml
+      # - ${PWD}/serve.toml:/serve.toml
     command: serve run
     ports:
       - "8080:7999"
