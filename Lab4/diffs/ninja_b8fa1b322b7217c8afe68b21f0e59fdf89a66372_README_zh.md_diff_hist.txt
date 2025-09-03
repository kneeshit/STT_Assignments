diff --git a/README_zh.md b/README_zh.md
index 8a89cf0..af974de 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -36,7 +36,7 @@
 1) 使用HAR
 
    - 支持HAR特征池化，可同时上传多个HAR，使用策略为随机请求。
-   > `ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-gpt4-har-dir` 指定HAR目录路径使用（不指定路径则使用默认路径`~/.chat4.openai.com.har`，可直接上传更新HAR），同理`GPT3.5`和其他类型也是一样方法。支持WebUI上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`。并且
+   > `ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-gpt4-har-dir` 指定HAR目录路径使用（不指定路径则使用默认路径`~/.gpt4`，可直接上传更新HAR），同理`GPT3.5`和其他类型也是一样方法。支持WebUI上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
 
 2) 使用[YesCaptcha](https://yescaptcha.com/i/1Cc5i4) / [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d)
    > 平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
@@ -51,16 +51,16 @@
 #### 公开接口, `*` 表示任意`URL`后缀
 
 - ChatGPT-API
-  - <https://host:port/public-api/*>
-  - <https://host:port/backend-api/*>
+  - `/public-api/*`
+  - `/backend-api/*`
   
 - OpenAI-API
-  - <https://host:port/v1/*>
+  - `/v1/*>`
 
 - Platform-API
-  - <https://host:port/dashboard/*>
+  - `/dashboard/*`
 - ChatGPT-To-API
-  - <https://host:port/to/v1/chat/completions>
+  - `/to/v1/chat/completions`
   > 关于`ChatGPT`转`API`使用方法，`AceessToken`当`API Key`使用
 
 #### API文档
