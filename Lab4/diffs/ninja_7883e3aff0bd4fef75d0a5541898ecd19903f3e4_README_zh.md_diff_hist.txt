diff --git a/README_zh.md b/README_zh.md
index 5e1ff5b..60296d3 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -97,8 +97,8 @@
   GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.6.6/ninja-0.6.6-x86_64-unknown-linux-musl.deb
-dpkg -i ninja-0.6.6-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.6.7/ninja-0.6.7-x86_64-unknown-linux-musl.deb
+dpkg -i ninja-0.6.7-x86_64-unknown-linux-musl.deb
 ninja serve run
 ```
 
@@ -107,11 +107,11 @@ ninja serve run
 GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.6.6/ninja_0.6.6_aarch64_generic.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.6.6/luci-app-ninja_1.1.3-1_all.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.6.6/luci-i18n-ninja-zh-cn_1.1.3-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.7/ninja_0.6.7_aarch64_generic.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.7/luci-app-ninja_1.1.3-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.7/luci-i18n-ninja-zh-cn_1.1.3-1_all.ipk
 
-opkg install ninja_0.6.6_aarch64_generic.ipk
+opkg install ninja_0.6.7_aarch64_generic.ipk
 opkg install luci-app-ninja_1.1.3-1_all.ipk
 opkg install luci-i18n-ninja-zh-cn_1.1.3-1_all.ipk
 ```
