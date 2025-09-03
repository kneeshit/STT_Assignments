diff --git a/README.md b/README.md
index 189f776..68d6606 100644
--- a/README.md
+++ b/README.md
@@ -24,6 +24,22 @@ A reverse engineered unofficial `ChatGPT` proxy (bypass Cloudflare 403 Access De
 
 > Limitations: This cannot bypass OpenAI's outright IP ban
 
+### Platform Support
+
+- Linux musl current supports
+  - `x86_64-unknown-linux-musl`
+  - `aarch64-unknown-linux-musl`
+  - `armv7-unknown-linux-musleabi`
+  - `armv7-unknown-linux-musleabihf`
+  - `arm-unknown-linux-musleabi`
+  - `arm-unknown-linux-musleabihf`
+  - `armv5te-unknown-linux-musleabi`
+- Windows current supports
+  - `x86_64-pc-windows-msvc`
+- MacOS current supports
+  - `x86_64-apple-darwin`
+  - `aarch64-apple-darwin`
+
 ### Install
 
   > #### Ubuntu(Other Linux)
@@ -31,11 +47,11 @@ A reverse engineered unofficial `ChatGPT` proxy (bypass Cloudflare 403 Access De
 Making [Releases](https://github.com/gngpp/opengpt/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.7/opengpt-0.1.7-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.8/opengpt-0.1.8-x86_64-unknown-linux-musl.deb
 
-dpkg -i opengpt-0.1.7-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.1.8-x86_64-unknown-linux-musl.deb
 
-opengpt serve
+opengpt serve run
 ```
 
 > #### Docker
@@ -44,7 +60,7 @@ opengpt serve
 docker run --rm -it -p 7999:7999 --hostname=opengpt \
   -e OPENGPT_WORKERS=1 \
   -e OPENGPT_LOG_LEVEL=info \
-  gngpp/opengpt:latest serve
+  gngpp/opengpt:latest serve run
 ```
 
 > #### OpenWrt
@@ -52,11 +68,11 @@ docker run --rm -it -p 7999:7999 --hostname=opengpt \
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.7/opengpt_0.1.7_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.7/luci-app-opengpt_1.0.2-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.7/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.8/opengpt_0.1.8_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.8/luci-app-opengpt_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.8/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
-opkg install opengpt_0.1.7_aarch64_generic.ipk
+opkg install opengpt_0.1.8_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.2-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 ```
@@ -86,7 +102,7 @@ opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 $ opengpt serve --help
 Start the http server
 
-Usage: opengpt serve [OPTIONS]
+Usage: opengpt serve run [OPTIONS]
 
 Options:
   -H, --host <HOST>
@@ -123,18 +139,6 @@ Options:
 
 ### Compile
 
-- Linux musl current supports
-  - `x86_64-unknown-linux-musl`
-  - `aarch64-unknown-linux-musl`
-  - `armv7-unknown-linux-musleabi`
-  - `armv7-unknown-linux-musleabihf`
-  - `arm-unknown-linux-musleabi`
-  - `arm-unknown-linux-musleabihf`
-  - `armv5te-unknown-linux-musleabi`
-  - `x86_64-pc-windows-msvc`
-  - `x86_64-apple-darwin`
-  - `aarch64-apple-darwin`
-
 - Linux compile, Ubuntu machine for example:
 
 ```shell
