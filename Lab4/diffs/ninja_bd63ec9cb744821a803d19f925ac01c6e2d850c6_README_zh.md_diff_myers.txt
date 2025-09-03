diff --git a/README_zh.md b/README_zh.md
index 67dcea9..253f63e 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -93,7 +93,7 @@
 ```shell
 wget https://github.com/gngpp/ninja/releases/download/v0.7.1/ninja-0.7.1-x86_64-unknown-linux-musl.deb
 dpkg -i ninja-0.7.1-x86_64-unknown-linux-musl.deb
-ninja serve run
+ninja run
 ```
 
 - #### OpenWrt
@@ -116,7 +116,7 @@ opkg install luci-i18n-ninja-zh-cn_1.1.3-1_all.ipk
 docker run --rm -it -p 7999:7999 --name=ninja \
   -e WORKERS=1 \
   -e LOG=info \
-  gngpp/ninja:latest serve run
+  gngpp/ninja:latest run
 ```
 
 - Docker Compose
@@ -142,7 +142,7 @@ services:
     # volumes:
       # - ${PWD}/ssl:/etc
       # - ${PWD}/serve.toml:/serve.toml
-    command: serve run
+    command: run
     ports:
       - "8080:7999"
     depends_on:
