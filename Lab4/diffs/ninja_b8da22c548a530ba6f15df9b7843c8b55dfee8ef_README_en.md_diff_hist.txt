diff --git a/README_en.md b/README_en.md
index 5231eff..3f74a25 100644
--- a/README_en.md
+++ b/README_en.md
@@ -41,22 +41,6 @@ Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter,
 - All three solutions are used, the priority is: `HAR` > `YesCaptcha/CapSolver` > `Arkose Token endpoint`
 - `YesCaptcha/CapSolver` is recommended to be used with HAR. When the verification code is generated, the parser is called for processing. After verification, HAR is more durable.
 
-### Platform Support
-
-- Linux
-  - `x86_64-unknown-linux-musl`
-  - `aarch64-unknown-linux-musl`
-  - `armv7-unknown-linux-musleabi`
-  - `armv7-unknown-linux-musleabihf`
-  - `arm-unknown-linux-musleabi`
-  - `arm-unknown-linux-musleabihf`
-  - `armv5te-unknown-linux-musleabi`
-- Windows
-  - `x86_64-pc-windows-msvc`
-- MacOS
-  - `x86_64-apple-darwin`
-  - `aarch64-apple-darwin`
-
 ### Command Line(dev)
 
 ### Http Server
@@ -116,12 +100,12 @@ There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/n
 
 ```shell
 wget https://github.com/gngpp/ninja/releases/download/v0.5.4/ninja_0.5.4_aarch64_generic.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.5.4/luci-app-ninja_1.0.6-1_all.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.5.4/luci-i18n-ninja-zh-cn_1.0.6-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.5.4/luci-app-ninja_1.0.9-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.5.4/luci-i18n-ninja-zh-cn_1.0.9-1_all.ipk
 
 opkg install ninja_0.5.4_aarch64_generic.ipk
-opkg install luci-app-ninja_1.0.6-1_all.ipk
-opkg install luci-i18n-ninja-zh-cn_1.0.6-1_all.ipk
+opkg install luci-app-ninja_1.0.9-1_all.ipk
+opkg install luci-i18n-ninja-zh-cn_1.0.9-1_all.ipk
 ```
 
 - #### Docker
@@ -135,6 +119,8 @@ docker run --rm -it -p 7999:7999 --name=ninja \
 
 - Docker Compose
 
+> `CloudFlare Warp` is not supported in your region (China), please delete it, or if your `VPS` IP can be directly connected to `OpenAI`, you can also delete it
+
 ```yaml
 version: '3'
 
@@ -252,6 +238,22 @@ Options:
           Print help
 ```
 
+### Platform Support
+
+- Linux
+  - `x86_64-unknown-linux-musl`
+  - `aarch64-unknown-linux-musl`
+  - `armv7-unknown-linux-musleabi`
+  - `armv7-unknown-linux-musleabihf`
+  - `arm-unknown-linux-musleabi`
+  - `arm-unknown-linux-musleabihf`
+  - `armv5te-unknown-linux-musleabi`
+- Windows
+  - `x86_64-pc-windows-msvc`
+- MacOS
+  - `x86_64-apple-darwin`
+  - `aarch64-apple-darwin`
+
 ### Compile
 
 - Linux compile, Ubuntu machine for example:
