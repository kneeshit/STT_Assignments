diff --git a/README.md b/README.md
index 348ef5a..c6bbdd4 100644
--- a/README.md
+++ b/README.md
@@ -102,8 +102,8 @@ Sending `GPT4/GPT-3.5 (already grayscale)/Creating API-Key` dialog requires send
 Making [Releases](https://github.com/gngpp/ninja/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.7.4/ninja-0.7.4-x86_64-unknown-linux-musl.deb
-dpkg -i ninja-0.7.4-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.7.4/ninja-0.7.5-x86_64-unknown-linux-musl.deb
+dpkg -i ninja-0.7.5-x86_64-unknown-linux-musl.deb
 ninja run
 ```
 
@@ -113,12 +113,12 @@ There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/n
 
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
