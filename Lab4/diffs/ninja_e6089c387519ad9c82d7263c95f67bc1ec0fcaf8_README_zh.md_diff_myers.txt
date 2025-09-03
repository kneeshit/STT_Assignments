diff --git a/README_zh.md b/README_zh.md
index 5e8a895..21cfc32 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -62,8 +62,8 @@
   GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.4.5/opengpt-0.4.5-x86_64-unknown-linux-musl.deb
-dpkg -i opengpt-0.4.5-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.4.6/opengpt-0.4.6-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.4.6-x86_64-unknown-linux-musl.deb
 opengpt serve run
 ```
 
@@ -72,11 +72,11 @@ opengpt serve run
 GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.4.5/opengpt_0.4.5_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.4.5/luci-app-opengpt_1.0.6-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.4.5/luci-i18n-opengpt-zh-cn_1.0.6-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.4.6/opengpt_0.4.6_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.4.6/luci-app-opengpt_1.0.6-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.4.6/luci-i18n-opengpt-zh-cn_1.0.6-1_all.ipk
 
-opkg install opengpt_0.4.5_aarch64_generic.ipk
+opkg install opengpt_0.4.6_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.6-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.6-1_all.ipk
 ```
