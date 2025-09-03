diff --git a/README.md b/README.md
index f9a9ec2..7df77b6 100644
--- a/README.md
+++ b/README.md
@@ -98,8 +98,8 @@ Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter,
 Making [Releases](https://github.com/gngpp/ninja/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.6.6/ninja-0.6.6-x86_64-unknown-linux-musl.deb
-dpkg -i ninja-0.6.6-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.6.7/ninja-0.6.7-x86_64-unknown-linux-musl.deb
+dpkg -i ninja-0.6.7-x86_64-unknown-linux-musl.deb
 ninja serve run
 ```
 
@@ -108,11 +108,11 @@ ninja serve run
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/ninja/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
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
