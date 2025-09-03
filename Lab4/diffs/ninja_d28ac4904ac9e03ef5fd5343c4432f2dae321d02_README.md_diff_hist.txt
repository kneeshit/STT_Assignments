diff --git a/README.md b/README.md
index b70a387..b6dd546 100644
--- a/README.md
+++ b/README.md
@@ -51,8 +51,8 @@ A reverse engineered unofficial `ChatGPT` proxy (bypass Cloudflare 403 Access De
 Making [Releases](https://github.com/gngpp/opengpt/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.4/opengpt-0.3.4-x86_64-unknown-linux-musl.deb
-dpkg -i opengpt-0.3.4-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.5/opengpt-0.3.5-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.3.5-x86_64-unknown-linux-musl.deb
 opengpt serve run
 ```
 
@@ -126,11 +126,11 @@ services:
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.4/opengpt_0.3.4_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.4/luci-app-opengpt_1.0.2-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.4/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.5/opengpt_0.3.5_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.5/luci-app-opengpt_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.5/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
-opkg install opengpt_0.3.4_aarch64_generic.ipk
+opkg install opengpt_0.3.5_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.2-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 ```
