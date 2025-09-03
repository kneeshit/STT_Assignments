diff --git a/README.md b/README.md
index 4f9e3c6..ea8dae9 100644
--- a/README.md
+++ b/README.md
@@ -51,9 +51,9 @@ docker run --rm -it -p 7999:7999 --hostname=opengpt \
 GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/xunlei/releases/download/v0.1.2/opengpt_0.1.2_aarch64_generic.ipk
-wget https://github.com/gngpp/xunlei/releases/download/v0.1.2/luci-app-opengpt_1.0.0-1_all.ipk
-wget https://github.com/gngpp/xunlei/releases/download/v0.1.2/luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/opengpt_0.1.2_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/luci-app-opengpt_1.0.0-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
 
 opkg install opengpt_0.1.2_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.0-1_all.ipk
