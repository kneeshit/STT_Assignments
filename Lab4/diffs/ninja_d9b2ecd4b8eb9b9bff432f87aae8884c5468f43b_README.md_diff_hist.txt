diff --git a/README.md b/README.md
index e5834c0..6aff3eb 100644
--- a/README.md
+++ b/README.md
@@ -97,8 +97,8 @@ Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter,
 Making [Releases](https://github.com/gngpp/ninja/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.5.7/ninja-0.5.7-x86_64-unknown-linux-musl.deb
-dpkg -i ninja-0.5.7-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.5.8/ninja-0.5.8-x86_64-unknown-linux-musl.deb
+dpkg -i ninja-0.5.8-x86_64-unknown-linux-musl.deb
 ninja serve run
 ```
 
@@ -107,11 +107,11 @@ ninja serve run
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/ninja/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
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
@@ -214,8 +214,12 @@ Options:
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
