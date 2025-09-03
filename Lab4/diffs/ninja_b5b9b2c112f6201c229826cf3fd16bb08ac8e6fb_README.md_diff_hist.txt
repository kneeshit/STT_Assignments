diff --git a/README.md b/README.md
index 1681fb4..eec74ee 100644
--- a/README.md
+++ b/README.md
@@ -17,10 +17,13 @@
 
 A reverse engineered unofficial `ChatGPT` proxy (bypass Cloudflare 403 Access Denied)
 
+###  Features
+
 - API key acquisition
 - Email/password account authentication (Google/Microsoft third-party login is not supported for now because the author does not have an account)
 - Unofficial/Official Http API proxy (for third-party client access)
 - The original ChatGPT WebUI
+- Minimal memory usage
 
 > Limitations: This cannot bypass OpenAI's outright IP ban
 
@@ -47,9 +50,9 @@ A reverse engineered unofficial `ChatGPT` proxy (bypass Cloudflare 403 Access De
 Making [Releases](https://github.com/gngpp/opengpt/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.5/opengpt-0.2.5-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/opengpt-0.2.6-x86_64-unknown-linux-musl.deb
 
-dpkg -i opengpt-0.2.5-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.2.6-x86_64-unknown-linux-musl.deb
 
 opengpt serve run
 ```
@@ -68,11 +71,11 @@ docker run --rm -it -p 7999:7999 --hostname=opengpt \
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.5/opengpt_0.2.5_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.5/luci-app-opengpt_1.0.2-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.5/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/opengpt_0.2.6_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/luci-app-opengpt_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
-opkg install opengpt_0.2.5_aarch64_generic.ipk
+opkg install opengpt_0.2.6_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.2-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 ```
