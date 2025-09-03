diff --git a/README.md b/README.md
index beff057..157921e 100644
--- a/README.md
+++ b/README.md
@@ -104,8 +104,8 @@
   GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.5.3/ninja-0.5.3-x86_64-unknown-linux-musl.deb
-dpkg -i ninja-0.5.3-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.5.4/ninja-0.5.4-x86_64-unknown-linux-musl.deb
+dpkg -i ninja-0.5.4-x86_64-unknown-linux-musl.deb
 ninja serve run
 ```
 
@@ -114,11 +114,11 @@ ninja serve run
 GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.5.3/ninja_0.5.3_aarch64_generic.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.5.3/luci-app-ninja_1.0.6-1_all.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.5.3/luci-i18n-ninja-zh-cn_1.0.6-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.5.4/ninja_0.5.4_aarch64_generic.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.5.4/luci-app-ninja_1.0.6-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.5.4/luci-i18n-ninja-zh-cn_1.0.6-1_all.ipk
 
-opkg install ninja_0.5.3_aarch64_generic.ipk
+opkg install ninja_0.5.4_aarch64_generic.ipk
 opkg install luci-app-ninja_1.0.6-1_all.ipk
 opkg install luci-i18n-ninja-zh-cn_1.0.6-1_all.ipk
 ```
