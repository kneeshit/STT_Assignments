diff --git a/README.md b/README.md
index 37688d4..88e7ba8 100644
--- a/README.md
+++ b/README.md
@@ -32,7 +32,7 @@
 
 发送`GPT4`对话需要`Arkose Token`作为参数发送，支持的解决方案暂时只有三种
 
-1) `Arkose Token` 获取的端点，不管你用什么方式，使用 `--arkose-token-endpoint` 指定端点获取token，支持的`JSON`格式，一般按照社区的格式：`{"token":"xxxxxx"}`
+1) 获取`Arkose Token`的端点，不管你用什么方式，使用 `--arkose-token-endpoint` 指定端点获取token，支持的`JSON`格式，一般按照社区的格式：`{"token":"xxxxxx"}`
 
 2) 使用HAR，`ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-har-file` 指定HAR文件路径使用(不指定路径则使用默认路径，可直接上传更新HAR)，支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
 
