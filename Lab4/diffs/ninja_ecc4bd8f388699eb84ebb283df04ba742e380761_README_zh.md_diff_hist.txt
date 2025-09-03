diff --git a/README_zh.md b/README_zh.md
index 4945e07..1013a7c 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -24,6 +24,22 @@
 
 > 局限性: 无法绕过 OpenAI 的彻底 IP 禁令
 
+### 平台支持
+
+- Linux musl 目前支持
+  - `x86_64-unknown-linux-musl`
+  - `aarch64-unknown-linux-musl`
+  - `armv7-unknown-linux-musleabi`
+  - `armv7-unknown-linux-musleabihf`
+  - `arm-unknown-linux-musleabi`
+  - `arm-unknown-linux-musleabihf`
+  - `armv5te-unknown-linux-musleabi`
+- Windows 目前支持
+  - `x86_64-pc-windows-msvc`
+- MacOS 目前支持
+  - `x86_64-apple-darwin`
+  - `aarch64-apple-darwin`
+
 ### 安装
   >
   > #### Ubuntu(Other Linux)
@@ -31,11 +47,11 @@
   GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
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
 GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
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
 
 ### 自行编译
 
-- Linux musl 目前支持
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
 - Linux编译，Ubuntu机器为例:
 
 ```shell
