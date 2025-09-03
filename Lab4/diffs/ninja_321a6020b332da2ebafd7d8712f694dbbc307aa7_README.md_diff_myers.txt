diff --git a/README.md b/README.md
index 4b8a3a3..362886b 100644
--- a/README.md
+++ b/README.md
@@ -28,6 +28,14 @@
 
 > 局限性: 无法绕过 OpenAI 的彻底 IP 禁令
 
+### 绕过IP限制
+
+这里`IP限制`是指`OpenAI`对`单IP`请求速率限制，你需要了解什么是`puid`，默认请求models接口返回`puid cookie`。
+另外，`GPT-4`会话必须带上`puid`发送，在使用第三方客户端发送`GPT-4`回话时可能不会保存也不会获取`puid`，你需要在服务端处理:
+
+- 使用启动参数`--puid`单独设置共享使用，此方式不支持更新
+- 使用启动参数`--puid-user`，设置`Account Plus`账号来获取`puid`，并且会定时更新
+
 ### ArkoseLabs
 
 发送`GPT4`对话需要`Arkose Token`作为参数发送，支持的解决方案暂时只有三种
@@ -36,7 +44,7 @@
 
 2) 使用HAR，`ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-har-file` 指定HAR文件路径使用（不指定路径则使用默认路径`~/chat.openai.com.har`，可直接上传更新HAR），支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
 
-3) 使用[YesCaptcha](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/overview?homepageId=33020) / [CapSolver](https://docs.capsolver.com/guide/why-choose-capsolver.html)平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
+3) 使用[YesCaptcha](https://yescaptcha.com/i/1Cc5i4) / [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d)平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
 
 - 三种方案都使用，优先级是：`HAR` > `YesCaptcha` / `CapSolver` > `Arkose Token 端点`
 - `YesCaptcha` / `CapSolver`推荐搭配HAR使用，出验证码则调用解析器处理，验证后HAR使用更持久
