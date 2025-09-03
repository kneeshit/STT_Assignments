diff --git a/README_zh.md b/README_zh.md
index a9ad17c..a4336d8 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -96,8 +96,8 @@
   GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.5.7/ninja-0.5.7-x86_64-unknown-linux-musl.deb
-dpkg -i ninja-0.5.7-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.5.8/ninja-0.5.8-x86_64-unknown-linux-musl.deb
+dpkg -i ninja-0.5.8-x86_64-unknown-linux-musl.deb
 ninja serve run
 ```
 
@@ -106,11 +106,11 @@ ninja serve run
 GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.5.7/ninja_0.5.7_aarch64_generic.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.5.7/luci-app-ninja_1.0.9-1_all.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.5.7/luci-i18n-ninja-zh-cn_1.0.9-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.5.8/ninja_0.5.8_aarch64_generic.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.5.8/luci-app-ninja_1.0.9-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.5.8/luci-i18n-ninja-zh-cn_1.0.9-1_all.ipk
 
-opkg install ninja_0.5.7_aarch64_generic.ipk
+opkg install ninja_0.5.8_aarch64_generic.ipk
 opkg install luci-app-ninja_1.0.9-1_all.ipk
 opkg install luci-i18n-ninja-zh-cn_1.0.9-1_all.ipk
 ```
@@ -213,8 +213,12 @@ Options:
           Arkose endpoint, Example: https://client-api.arkoselabs.com
   -A, --arkose-token-endpoint <ARKOSE_TOKEN_ENDPOINT>
           Get arkose token endpoint
-  -a, --arkose-har-file <ARKOSE_HAR_FILE>
+      --arkose-chat-har-path <ARKOSE_CHAT_HAR_PATH>
           About the browser HAR file path requested by ChatGPT ArkoseLabs
+      --arkose-platform-har-path <ARKOSE_PLATFORM_HAR_PATH>
+          About the browser HAR file path requested by Platform ArkoseLabs
+      --arkose-auth-har-path <ARKOSE_AUTH_HAR_PATH>
+          About the browser HAR file path requested by Auth ArkoseLabs
   -K, --arkose-har-upload-key <ARKOSE_HAR_UPLOAD_KEY>
           HAR file upload authenticate key
   -s, --arkose-solver <ARKOSE_SOLVER>
