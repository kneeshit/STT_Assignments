diff --git a/README_zh.md b/README_zh.md
index 777ff5f..2850d46 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -103,8 +103,8 @@
   GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.7.4/ninja-0.7.4-x86_64-unknown-linux-musl.deb
-dpkg -i ninja-0.7.4-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.7.4/ninja-0.7.5-x86_64-unknown-linux-musl.deb
+dpkg -i ninja-0.7.5-x86_64-unknown-linux-musl.deb
 ninja run
 ```
 
@@ -114,12 +114,12 @@ GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编
 
 ```shell
 wget https://github.com/gngpp/ninja/releases/download/v0.7.4/ninja_0.7.4_aarch64_generic.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.7.4/luci-app-ninja_1.1.4-1_all.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.7.4/luci-i18n-ninja-zh-cn_1.1.4-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.7.4/luci-app-ninja_1.1.5-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.7.4/luci-i18n-ninja-zh-cn_1.1.5-1_all.ipk
 
 opkg install ninja_0.7.4_aarch64_generic.ipk
-opkg install luci-app-ninja_1.1.4-1_all.ipk
-opkg install luci-i18n-ninja-zh-cn_1.1.4-1_all.ipk
+opkg install luci-app-ninja_1.1.5-1_all.ipk
+opkg install luci-i18n-ninja-zh-cn_1.1.5-1_all.ipk
 ```
 
 - #### Docker
