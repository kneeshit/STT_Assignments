diff --git a/README.md b/README.md
index 6d23054..abb8e72 100644
--- a/README.md
+++ b/README.md
@@ -93,7 +93,7 @@ Making [Releases](https://github.com/gngpp/ninja/releases/latest) has a precompi
 ```shell
 wget https://github.com/gngpp/ninja/releases/download/v0.7.1/ninja-0.7.1-x86_64-unknown-linux-musl.deb
 dpkg -i ninja-0.7.1-x86_64-unknown-linux-musl.deb
-ninja serve run
+ninja run
 ```
 
 - #### OpenWrt
@@ -167,7 +167,6 @@ services:
 
 ```shell
 $ ninja --help
-$ ninja --help
 Reverse engineered ChatGPT proxy
 
 Usage: ninja [COMMAND]
