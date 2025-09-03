diff --git a/README_zh.md b/README_zh.md
index 2c19755..827fd11 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -98,8 +98,8 @@
   GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.6.1/ninja-0.6.1-x86_64-unknown-linux-musl.deb
-dpkg -i ninja-0.6.1-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.6.2/ninja-0.6.2-x86_64-unknown-linux-musl.deb
+dpkg -i ninja-0.6.2-x86_64-unknown-linux-musl.deb
 ninja serve run
 ```
 
@@ -108,11 +108,11 @@ ninja serve run
 GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.6.1/ninja_0.6.1_aarch64_generic.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.6.1/luci-app-ninja_1.0.9-1_all.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.6.1/luci-i18n-ninja-zh-cn_1.0.9-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.2/ninja_0.6.2_aarch64_generic.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.2/luci-app-ninja_1.0.9-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.2/luci-i18n-ninja-zh-cn_1.0.9-1_all.ipk
 
-opkg install ninja_0.6.1_aarch64_generic.ipk
+opkg install ninja_0.6.2_aarch64_generic.ipk
 opkg install luci-app-ninja_1.0.9-1_all.ipk
 opkg install luci-i18n-ninja-zh-cn_1.0.9-1_all.ipk
 ```
