diff --git a/README.md b/README.md
index 2d46efb..9ec1e0c 100644
--- a/README.md
+++ b/README.md
@@ -62,8 +62,8 @@ All three schemes are used, and the priority is: `HAR` > `Arkose Token endpoint`
 Making [Releases](https://github.com/gngpp/opengpt/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.4.5/opengpt-0.4.5-x86_64-unknown-linux-musl.deb
-dpkg -i opengpt-0.4.5-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.4.6/opengpt-0.4.6-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.4.6-x86_64-unknown-linux-musl.deb
 opengpt serve run
 ```
 
@@ -72,11 +72,11 @@ opengpt serve run
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
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
