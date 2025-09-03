diff --git a/README_zh.md b/README_zh.md
index ea20159..8a89cf0 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -114,7 +114,7 @@ ninja run --pbind 0.0.0.0:8888
   GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.7.4/ninja-0.7.5-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.7.5/ninja-0.7.5-x86_64-unknown-linux-musl.deb
 dpkg -i ninja-0.7.5-x86_64-unknown-linux-musl.deb
 ninja run
 ```
@@ -124,11 +124,11 @@ ninja run
 GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.7.4/ninja_0.7.4_aarch64_generic.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.7.4/luci-app-ninja_1.1.5-1_all.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.7.4/luci-i18n-ninja-zh-cn_1.1.5-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.7.5/ninja_0.7.5_aarch64_generic.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.7.5/luci-app-ninja_1.1.5-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.7.5/luci-i18n-ninja-zh-cn_1.1.5-1_all.ipk
 
-opkg install ninja_0.7.4_aarch64_generic.ipk
+opkg install ninja_0.7.5_aarch64_generic.ipk
 opkg install luci-app-ninja_1.1.5-1_all.ipk
 opkg install luci-i18n-ninja-zh-cn_1.1.5-1_all.ipk
 ```
