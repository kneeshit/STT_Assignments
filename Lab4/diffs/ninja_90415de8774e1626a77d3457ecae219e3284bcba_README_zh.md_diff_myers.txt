diff --git a/README_zh.md b/README_zh.md
index 1bedaa5..0539de5 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -134,14 +134,6 @@ services:
     environment:
       - TZ=Asia/Shanghai
       - PROXIES=socks5://warp:10000
-      # - CONFIG=/serve.toml
-      # - PORT=8080
-      # - HOST=0.0.0.0
-      # - TLS_CERT=
-      # - TLS_KEY=
-    # volumes:
-      # - ${PWD}/ssl:/etc
-      # - ${PWD}/serve.toml:/serve.toml
     command: run
     ports:
       - "8080:7999"
