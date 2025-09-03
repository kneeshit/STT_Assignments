diff --git a/README.md b/README.md
index 157921e..4b8a3a3 100644
--- a/README.md
+++ b/README.md
@@ -41,22 +41,6 @@
 - 三种方案都使用，优先级是：`HAR` > `YesCaptcha` / `CapSolver` > `Arkose Token 端点`
 - `YesCaptcha` / `CapSolver`推荐搭配HAR使用，出验证码则调用解析器处理，验证后HAR使用更持久
 
-### 平台支持
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
 
 ### Http 服务
@@ -115,12 +99,12 @@ GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编
 
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
@@ -134,6 +118,8 @@ docker run --rm -it -p 7999:7999 --name=ninja \
 
 - Docker Compose
 
+> `CloudFlare Warp`你的地区不支持（China）请把它删掉，或者你的`VPS`IP可直连`OpenAI`，那么也可以删掉
+
 ```yaml
 version: '3'
 
@@ -251,6 +237,22 @@ Options:
           Print help
 ```
 
+### 平台支持
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
 ### 编译
 
 - Linux编译，Ubuntu机器为例:
