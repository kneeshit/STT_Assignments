diff --git a/README.md b/README.md
index 007b51a..00e5bed 100644
--- a/README.md
+++ b/README.md
@@ -31,7 +31,7 @@
 ### 绕过IP限制
 
 这里`IP限制`是指`OpenAI`对`单IP`请求速率限制，你需要了解什么是`puid`，默认请求models接口返回`puid cookie`。
-另外，`GPT-4`会话必须带上`puid`发送，在使用第三方客户端发送`GPT-4`回话时可能不会保存也不会获取`puid`，你需要在服务端处理:
+另外，`GPT-4`会话必须带上`puid`发送，在使用第三方客户端发送`GPT-4`会话时可能不会保存也不会获取`puid`，你需要在服务端处理:
 
 - 使用启动参数`--puid`单独设置共享使用，此方式不支持更新
 - 使用启动参数`--puid-user`，设置`Account Plus`账号来获取`puid`，并且会定时更新
