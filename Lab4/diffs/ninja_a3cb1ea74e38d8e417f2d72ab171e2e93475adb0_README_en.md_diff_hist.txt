diff --git a/README_en.md b/README_en.md
index d7870fc..87dc028 100644
--- a/README_en.md
+++ b/README_en.md
@@ -51,9 +51,9 @@ docker run --rm -it -p 7999:7999 --hostname=opengpt \
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
 ```shell
-wget https://github.com/gngpp/xunlei/releases/download/v0.1.2/opengpt_0.1.2_aarch64_generic.ipk
-wget https://github.com/gngpp/xunlei/releases/download/v0.1.2/luci-app-opengpt_1.0.0-1_all.ipk
-wget https://github.com/gngpp/xunlei/releases/download/v0.1.2/luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/opengpt_0.1.2_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/luci-app-opengpt_1.0.0-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
 
 opkg install opengpt_0.1.2_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.0-1_all.ipk
