diff --git a/README_zh.md b/README_zh.md
index c73d2dd..a4b2eb0 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -30,9 +30,9 @@
   GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/opengpt-0.1.2-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.6/opengpt-0.1.6-x86_64-unknown-linux-musl.deb
 
-dpkg -i opengpt-0.1.2-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.1.6-x86_64-unknown-linux-musl.deb
 
 opengpt serve
 ```
@@ -53,11 +53,11 @@ docker run --rm -it -p 7999:7999 --hostname=opengpt \
 GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/opengpt_0.1.2_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/luci-app-opengpt_1.0.0-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.6/opengpt_0.1.6_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.6/luci-app-opengpt_1.0.0-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.6/luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
 
-opkg install opengpt_0.1.2_aarch64_generic.ipk
+opkg install opengpt_0.1.6_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.0-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
 ```
@@ -133,6 +133,8 @@ Options:
   - `arm-unknown-linux-musleabihf`
   - `armv5te-unknown-linux-musleabi`
   - `x86_64-pc-windows-msvc`
+  - `x86_64-apple-darwin`
+  - `aarch64-apple-darwin`
 
 - Linux编译，Ubuntu机器为例:
 
