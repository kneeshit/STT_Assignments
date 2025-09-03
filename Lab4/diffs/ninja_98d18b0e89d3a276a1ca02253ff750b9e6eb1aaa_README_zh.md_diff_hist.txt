diff --git a/README_zh.md b/README_zh.md
index 420b052..7bf3117 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -34,12 +34,12 @@
 
 1) `Arkose Token` 获取的端点，不管你用什么方式，使用 `--arkose-token-endpoint` 指定端点获取token，支持的`JSON`格式，一般按照社区的格式：`{"token":"xxxxxx"}`
 
-2) `ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-har-file` 指定HAR文件路径使用。支持上传更新HAR `请求路径: /har/upload`，HAR文件是必须是存在的，此时才支持上传更新HAR文件，可选上传身份验证参数 `--arkose-har-upload-key`
+2) 使用HAR，`ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-har-file` 指定HAR文件路径使用(不指定路径则使用默认路径，可直接上传更新HAR)，支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
 
 3) 使用[YesCaptcha](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/overview?homepageId=33020) / [CapSolver](https://docs.capsolver.com/guide/why-choose-capsolver.html)平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
 
-- 三种方案都使用，优先级是：`HAR` > `YesCaptcha/CapSolver` > `Arkose Token 端点`
-- `YesCaptcha/CapSolver`推荐搭配HAR使用，出验证码则调用解析器处理，验证后HAR使用更持久
+- 三种方案都使用，优先级是：`HAR` > `YesCaptcha` / `CapSolver` > `Arkose Token 端点`
+- `YesCaptcha` / `CapSolver`推荐搭配HAR使用，出验证码则调用解析器处理，验证后HAR使用更持久
 
 ### 平台支持
 
