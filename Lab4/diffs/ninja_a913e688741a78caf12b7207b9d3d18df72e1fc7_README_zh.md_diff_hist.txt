diff --git a/README_zh.md b/README_zh.md
index 9c35922..759d3ba 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -73,6 +73,8 @@
 >
 > - Platfrom API [doc](https://platform.openai.com/docs/api-reference)
 > - Backend API [doc](doc/rest.http)
+>
+> 关于关于`ChatGPT`转`API`使用，直接拿`AceessToken`当`API Key`使用，接口路径`https://host:port/to/v1/chat/completions`
 
 - 原汁原味ChatGPT WebUI
 - 公开`非官方`/`官方API`代理
@@ -87,10 +89,10 @@
   - `--port`，环境变量 `PORT`， 监听端口: 默认7999
   - `--tls-cert`，环境变量 `TLS_CERT`，TLS证书公钥，支持格式: EC/PKCS8/RSA
   - `--tls-key`，环境变量 `TLS_KEY`，TLS证书私钥
-  - `--proxies`，代理，支持代理池，多个代理使用`,`隔开，格式: protocol://user:pass@ip:port, 如果IP被Ban，使用代理池时建议关闭直连IP使用，`--disable-direct`关闭直连
+  - `--proxies`，代理，支持代理池，多个代理使用`,`隔开，格式: protocol://user:pass@ip:port，如果本地IP被Ban，使用代理池时需要关闭直连IP使用，`--disable-direct`关闭直连，否则会根据负载均衡使用你被Ban的本地IP
   - `--workers`， 工作线程: 默认1
 
-...
+[...](https://github.com/gngpp/ninja/blob/main/README_zh.md#%E5%91%BD%E4%BB%A4%E6%89%8B%E5%86%8C)
 
 ### 安装
 
