diff --git a/README_zh.md b/README_zh.md
index 9d30750..a48a634 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -50,8 +50,8 @@
   GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.1/opengpt-0.3.1-x86_64-unknown-linux-musl.deb
-dpkg -i opengpt-0.3.1-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.2/opengpt-0.3.2-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.3.2-x86_64-unknown-linux-musl.deb
 opengpt serve run
 ```
 
@@ -125,11 +125,11 @@ services:
 GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.1/opengpt_0.3.1_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.1/luci-app-opengpt_1.0.2-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.1/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.2/opengpt_0.3.2_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.2/luci-app-opengpt_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.2/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
-opkg install opengpt_0.3.1_aarch64_generic.ipk
+opkg install opengpt_0.3.2_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.2-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 ```
