diff --git a/README_en.md b/README_en.md
index dce6571..5231eff 100644
--- a/README_en.md
+++ b/README_en.md
@@ -105,8 +105,8 @@ Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter,
 Making [Releases](https://github.com/gngpp/ninja/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.5.3/ninja-0.5.3-x86_64-unknown-linux-musl.deb
-dpkg -i ninja-0.5.3-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.5.4/ninja-0.5.4-x86_64-unknown-linux-musl.deb
+dpkg -i ninja-0.5.4-x86_64-unknown-linux-musl.deb
 ninja serve run
 ```
 
@@ -115,11 +115,11 @@ ninja serve run
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/ninja/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
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
