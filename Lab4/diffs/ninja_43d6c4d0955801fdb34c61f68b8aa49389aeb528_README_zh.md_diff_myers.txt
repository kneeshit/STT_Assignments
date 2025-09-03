diff --git a/README_zh.md b/README_zh.md
index 258e6e2..f52195f 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -36,9 +36,10 @@
 
 2) `ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-har-path` 指定HAR文件路径使用。支持上传更新HAR `请求路径: /har/upload`，HAR文件是必须是存在的，此时才支持上传更新HAR文件，可选上传身份验证参数 `--arkose-har-upload-key`
 
-3) 使用[YesCaptcha](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/overview?homepageId=33020)平台进行AI打码，启动参数 `--arkose-yescaptcha-key` 填写Key启用，价格实惠，`10RMB` 按积分提交来计算，`10000/3 ~= 3333 次提交`，
+3) 使用[YesCaptcha](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/overview?homepageId=33020)/[CapSolver](https://docs.capsolver.com/guide/why-choose-capsolver.html)平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
 
-三种方案都使用，优先级是：`HAR` > `Arkose Token 端点` > `YesCaptcha`
+- 三种方案都使用，优先级是：`HAR` > `YesCaptcha/CapSolver` > `Arkose Token 端点`
+- `YesCaptcha/CapSolver`推荐搭配HAR使用，出验证码则调用解析器处理，验证后HAR使用更持久
 
 ### 平台支持
 
@@ -213,12 +214,14 @@ Options:
           Arkose endpoint, Example: https://client-api.arkoselabs.com
   -A, --arkose-token-endpoint <ARKOSE_TOKEN_ENDPOINT>
           Get arkose token endpoint
-  -a, --arkose-har-path <ARKOSE_HAR_PATH>
+  -a, --arkose-har-file <ARKOSE_HAR_FILE>
           About the browser HAR file path requested by ArkoseLabs
   -K, --arkose-har-upload-key <ARKOSE_HAR_UPLOAD_KEY>
           HAR file upload authenticate key
-  -Y, --arkose-yescaptcha-key <ARKOSE_YESCAPTCHA_KEY>
-          About the YesCaptcha platform client key solved by ArkoseLabs
+  -s, --arkose-solver <ARKOSE_SOLVER>
+          About ArkoseLabs solver platform [default: yescaptcha]
+  -k, --arkose-solver-key <ARKOSE_SOLVER_KEY>
+          About the solver client key by ArkoseLabs
   -S, --sign-secret-key <SIGN_SECRET_KEY>
           Enable url signature (signature secret key)
   -T, --tb-enable
@@ -226,7 +229,7 @@ Options:
       --tb-store-strategy <TB_STORE_STRATEGY>
           Token bucket store strategy (mem/redis) [default: mem]
       --tb-redis-url <TB_REDIS_URL>
-          Token bucket redis url, Example: redis://user:pass@ip:port [default: redis://127.0.0.1:6379]
+          Token bucket redis connection url [default: redis://127.0.0.1:6379]
       --tb-capacity <TB_CAPACITY>
           Token bucket capacity [default: 60]
       --tb-fill-rate <TB_FILL_RATE>
