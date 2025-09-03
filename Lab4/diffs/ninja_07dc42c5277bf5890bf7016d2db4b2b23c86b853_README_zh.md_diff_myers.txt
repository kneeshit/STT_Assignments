diff --git a/README_zh.md b/README_zh.md
index 30568bf..d7ac7aa 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -27,9 +27,22 @@
 
 > 局限性: 无法绕过 OpenAI 的彻底 IP 禁令
 
+### ArkoseLabs
+
+发送`GPT4`对话需要`Arkose Token`作为参数发送，支持的解决方案暂时只有三种
+
+1) `Arkose Token` 获取的端点，不管你用什么方式，使用`--arkose-token-endpoint` 指定端点获取token，支持的`JSON`格式，一般按照社区的格式：`{"token":"xxxxxx"}`
+
+
+2) `ChatGPT`官网发送一次`GPT4`会话消息，浏览器`F12`下载`https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147`接口的HAR日志记录文件，然后使用启动参数`--arkose-har-path`指定HAR文件路径使用
+
+3) 使用[YesCaptcha](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/overview?homepageId=33020)平台进行AI打码，价格实惠，`10RMB`按积分提交来计算，`10000/3 ~= 3333 次提交`
+
+以上三种方案都使用的话，优先级是：`HAR` > `Arkose Token 端点` > `YesCaptcha`
+
 ### 平台支持
 
-- Linux musl 目前支持
+- Linux 支持
   - `x86_64-unknown-linux-musl`
   - `aarch64-unknown-linux-musl`
   - `armv7-unknown-linux-musleabi`
@@ -37,14 +50,14 @@
   - `arm-unknown-linux-musleabi`
   - `arm-unknown-linux-musleabihf`
   - `armv5te-unknown-linux-musleabi`
-- Windows 目前支持
+- Windows 支持
   - `x86_64-pc-windows-msvc`
-- MacOS 目前支持
+- MacOS 支持
   - `x86_64-apple-darwin`
   - `aarch64-apple-darwin`
 
 ### 安装
-  >
+
   > #### Ubuntu(Other Linux)
 
   GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
