diff --git a/README_zh.md b/README_zh.md
index 680041c..5891f38 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -42,7 +42,7 @@
 
 1) 获取`Arkose Token`的端点，不管你用什么方式，使用 `--arkose-token-endpoint` 指定端点获取token，支持的`JSON`格式，一般按照社区的格式：`{"token":"xxxxxx"}`
 
-2) 使用HAR，`ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-chat-har-file` 指定HAR文件路径使用（不指定路径则使用默认路径`~/chat.openai.com.har`，可直接上传更新HAR），支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
+2) 使用HAR，`ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-chat-har-file` 指定HAR文件路径使用（不指定路径则使用默认路径`~/.chat.openai.com.har`，可直接上传更新HAR），支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
 
 3) 使用[YesCaptcha](https://yescaptcha.com/i/1Cc5i4) / [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d)平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
 
