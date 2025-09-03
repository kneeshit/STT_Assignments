diff --git a/README_zh.md b/README_zh.md
index e9dc56c..547e50b 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -33,13 +33,11 @@
 
 1) `Arkose Token` 获取的端点，不管你用什么方式，使用 `--arkose-token-endpoint` 指定端点获取token，支持的`JSON`格式，一般按照社区的格式：`{"token":"xxxxxx"}`
 
+2) `ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-har-path` 指定HAR文件路径使用。支持上传更新HAR `请求路径: /har/upload`，HAR文件是必须是存在的，此时才支持上传更新HAR文件，可选上传身份验证参数 `--arkose-har-upload-key`
 
-2) `ChatGPT`官网发送一次`GPT4`会话消息，浏览器`F12`下载`https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147`接口的HAR日志记录文件，然后使用启动参数`--arkose-har-path`指定HAR文件路径使用
+3) 使用[YesCaptcha](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/overview?homepageId=33020)平台进行AI打码，启动参数 `--arkose-yescaptcha-key` 填写Key启用，价格实惠，`10RMB` 按积分提交来计算，`10000/3 ~= 3333 次提交`，
 
-3) 使用[YesCaptcha](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/overview?homepageId=33020)平台进行AI打码，价格实惠，`10RMB`按积分提交来计算，`10000/3 ~= 3333 次提交`
-
-三种方案都使用，优先级是：`HAR` > `Arkose Token 端点` > `YesCaptcha`。
-支持上传更新HAR`请求路径: /har/upload`，启动必须添加HAR文件路径，并且文件是存在的，此时才支持上传更新HAR文件。
+三种方案都使用，优先级是：`HAR` > `Arkose Token 端点` > `YesCaptcha`
 
 ### 平台支持
 
@@ -212,8 +210,10 @@ Options:
           Get arkose token endpoint
   -a, --arkose-har-path <ARKOSE_HAR_PATH>
           About the browser HAR file path requested by ArkoseLabs
+  -K, --arkose-har-upload-key <ARKOSE_HAR_UPLOAD_KEY>
+          HAR file upload authenticate key
   -Y, --arkose-yescaptcha-key <ARKOSE_YESCAPTCHA_KEY>
-          About the yescaptcha platform client key solved by ArkoseLabs
+          About the YesCaptcha platform client key solved by ArkoseLabs
   -S, --sign-secret-key <SIGN_SECRET_KEY>
           Enable url signature (signature secret key)
   -T, --tb-enable
