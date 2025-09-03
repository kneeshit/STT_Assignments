diff --git a/README.md b/README.md
index 9c980b8..4a9cb91 100644
--- a/README.md
+++ b/README.md
@@ -30,9 +30,9 @@ Not just an unofficial ChatGPT proxy (bypass Cloudflare 403 Access Denied)
 Making [Releases](https://github.com/gngpp/opengpt/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/opengpt-0.1.2-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.6/opengpt-0.1.6-x86_64-unknown-linux-musl.deb
 
-dpkg -i opengpt-0.1.2-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.1.6-x86_64-unknown-linux-musl.deb
 
 opengpt serve
 ```
@@ -53,11 +53,11 @@ docker run --rm -it -p 7999:7999 --hostname=opengpt \
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/opengpt_0.1.2_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/luci-app-opengpt_1.0.0-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.6/opengpt_0.1.6_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.6/luci-app-opengpt_1.0.0-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.6/luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
 
-opkg install opengpt_0.1.2_aarch64_generic.ipk
+opkg install opengpt_0.1.6_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.0-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
 ```
@@ -133,6 +133,8 @@ Options:
   - `arm-unknown-linux-musleabihf`
   - `armv5te-unknown-linux-musleabi`
   - `x86_64-pc-windows-msvc`
+  - `x86_64-apple-darwin`
+  - `aarch64-apple-darwin`
 
 - Linux compile, Ubuntu machine for example:
 
