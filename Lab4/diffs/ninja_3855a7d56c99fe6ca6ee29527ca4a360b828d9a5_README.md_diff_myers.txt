diff --git a/README.md b/README.md
index 1158827..2292bae 100644
--- a/README.md
+++ b/README.md
@@ -50,9 +50,9 @@ A reverse engineered unofficial `ChatGPT` proxy (bypass Cloudflare 403 Access De
 Making [Releases](https://github.com/gngpp/opengpt/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/opengpt-0.2.6-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.7/opengpt-0.2.7-x86_64-unknown-linux-musl.deb
 
-dpkg -i opengpt-0.2.6-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.2.7-x86_64-unknown-linux-musl.deb
 
 opengpt serve run
 ```
@@ -127,11 +127,11 @@ services:
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/opengpt_0.2.6_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/luci-app-opengpt_1.0.2-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.7/opengpt_0.2.7_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.7/luci-app-opengpt_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.7/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
-opkg install opengpt_0.2.6_aarch64_generic.ipk
+opkg install opengpt_0.2.7_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.2-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 ```
