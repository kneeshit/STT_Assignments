diff --git a/README_zh.md b/README_zh.md
index a4336d8..680041c 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -42,13 +42,15 @@
 
 1) 获取`Arkose Token`的端点，不管你用什么方式，使用 `--arkose-token-endpoint` 指定端点获取token，支持的`JSON`格式，一般按照社区的格式：`{"token":"xxxxxx"}`
 
-2) 使用HAR，`ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-har-file` 指定HAR文件路径使用（不指定路径则使用默认路径`~/chat.openai.com.har`，可直接上传更新HAR），支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
+2) 使用HAR，`ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-chat-har-file` 指定HAR文件路径使用（不指定路径则使用默认路径`~/chat.openai.com.har`，可直接上传更新HAR），支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
 
 3) 使用[YesCaptcha](https://yescaptcha.com/i/1Cc5i4) / [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d)平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
 
 - 三种方案都使用，优先级是：`HAR` > `YesCaptcha` / `CapSolver` > `Arkose Token 端点`
 - `YesCaptcha` / `CapSolver`推荐搭配HAR使用，出验证码则调用解析器处理，验证后HAR使用更持久
 
+> 目前OpenAI已经更新登录需要验证`Arkose Token`，解决方式同GPT4，填写启动参数指定HAR文件`--arkose-auth-har-file`
+
 ### Command Line(dev)
 
 ### Http 服务
@@ -213,12 +215,12 @@ Options:
           Arkose endpoint, Example: https://client-api.arkoselabs.com
   -A, --arkose-token-endpoint <ARKOSE_TOKEN_ENDPOINT>
           Get arkose token endpoint
-      --arkose-chat-har-path <ARKOSE_CHAT_HAR_PATH>
+      --arkose-chat-har-file <ARKOSE_CHAT_HAR_FILE>
           About the browser HAR file path requested by ChatGPT ArkoseLabs
-      --arkose-platform-har-path <ARKOSE_PLATFORM_HAR_PATH>
-          About the browser HAR file path requested by Platform ArkoseLabs
-      --arkose-auth-har-path <ARKOSE_AUTH_HAR_PATH>
+      --arkose-auth-har-file <ARKOSE_AUTH_HAR_FILE>
           About the browser HAR file path requested by Auth ArkoseLabs
+      --arkose-platform-har-file <ARKOSE_PLATFORM_HAR_FILE>
+          About the browser HAR file path requested by Platform ArkoseLabs
   -K, --arkose-har-upload-key <ARKOSE_HAR_UPLOAD_KEY>
           HAR file upload authenticate key
   -s, --arkose-solver <ARKOSE_SOLVER>
