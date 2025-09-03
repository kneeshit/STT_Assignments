diff --git a/README_zh.md b/README_zh.md
index ef9b0f0..f3d8561 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -28,12 +28,6 @@
 
 > 局限性: 无法绕过 OpenAI 的彻底 IP 禁令
 
-### 绕过IP限制
-
-这里`IP限制`是指`OpenAI`对`单IP`请求速率限制，你需要了解什么是`puid`，默认请求models接口返回`puid cookie`。
-另外，`GPT-4`会话必须带上`puid`发送，在使用第三方客户端发送`GPT-4`会话时可能不会保存也不会获取`puid`，你需要在服务端处理:
-
-- 使用启动参数`--puid-user`，设置`Account Plus`账号来获取`puid`，并且会定时更新
 
 ### ArkoseLabs
 
@@ -231,8 +225,6 @@ Options:
           TLS certificate file path [env: TLS_CERT=]
       --tls-key <TLS_KEY>
           TLS private key file path (EC/PKCS8/RSA) [env: TLS_KEY=]
-      --puid-user <PUID_USER>
-          Obtain the PUID of the Plus account user, Example: `user:pass`
       --api-prefix <API_PREFIX>
           WebUI api prefix [env: API_PREFIX=]
       --preauth-api <PREAUTH_API>
