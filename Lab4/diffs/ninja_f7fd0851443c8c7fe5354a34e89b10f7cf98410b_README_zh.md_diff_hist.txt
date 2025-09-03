diff --git a/README_zh.md b/README_zh.md
index 7d63a33..3a31c0a 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -30,16 +30,18 @@
 
 ### ArkoseLabs
 
-发送`GPT4/GPT-3.5(已经灰度)`对话需要`Arkose Token`作为参数发送，支持的解决方案暂时只有三种
+发送`GPT4/GPT-3.5(已经灰度)/创建API-Key`对话需要`Arkose Token`作为参数发送，支持的解决方案暂时只有两种
 
-1) 使用HAR，`ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-chat4-har-file` 指定HAR文件路径使用（不指定路径则使用默认路径`~/.chat4.openai.com.har`，可直接上传更新HAR），支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
+1) 使用HAR
+   > `ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-chat4-har-file` 指定HAR文件路径使用（不指定路径则使用默认路径`~/.chat4.openai.com.har`，可直接上传更新HAR），支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
 
-2) 使用[YesCaptcha](https://yescaptcha.com/i/1Cc5i4) / [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d)平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
+2) 使用[YesCaptcha](https://yescaptcha.com/i/1Cc5i4) / [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d)
+   > 平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
 
-- 三种方案都使用，优先级是：`HAR` > `YesCaptcha` / `CapSolver` > `Arkose Token 端点`
+- 两种方案都使用，优先级是：`HAR` > `YesCaptcha` / `CapSolver`
 - `YesCaptcha` / `CapSolver`推荐搭配HAR使用，出验证码则调用解析器处理，验证后HAR使用更持久
 
-> 目前OpenAI已经更新登录需要验证`Arkose Token`，解决方式同GPT4，填写启动参数指定HAR文件`--arkose-auth-har-file`。不想上传，可以通过浏览器打码登录，非必需。
+> 目前OpenAI已经更新`登录`需要验证`Arkose Token`，解决方式同GPT4，填写启动参数指定HAR文件`--arkose-auth-har-file`。不想上传，可以通过浏览器打码登录，非必需。创建API-Key需要上传Platform相关的HAR特征文件，获取方式同上。
 
 ### Http 服务
 
