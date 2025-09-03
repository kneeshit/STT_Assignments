diff --git a/README_zh.md b/README_zh.md
index 3b02bf9..1da7d72 100644
--- a/README_zh.md
+++ b/README_zh.md
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
