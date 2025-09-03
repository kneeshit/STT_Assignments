diff --git a/README.md b/README.md
index 0ec578b..07a6af8 100644
--- a/README.md
+++ b/README.md
@@ -47,9 +47,9 @@ A reverse engineered unofficial `ChatGPT` proxy (bypass Cloudflare 403 Access De
 Making [Releases](https://github.com/gngpp/opengpt/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.0/opengpt-0.2.0-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.1/opengpt-0.2.1-x86_64-unknown-linux-musl.deb
 
-dpkg -i opengpt-0.2.0-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.2.1-x86_64-unknown-linux-musl.deb
 
 opengpt serve run
 ```
@@ -68,11 +68,11 @@ docker run --rm -it -p 7999:7999 --hostname=opengpt \
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.0/opengpt_0.2.0_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.0/luci-app-opengpt_1.0.2-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.0/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.1/opengpt_0.2.1_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.1/luci-app-opengpt_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.1/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
-opkg install opengpt_0.2.0_aarch64_generic.ipk
+opkg install opengpt_0.2.1_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.2-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 ```
