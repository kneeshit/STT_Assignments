diff --git a/README.md b/README.md
index 9716939..d146f57 100644
--- a/README.md
+++ b/README.md
@@ -21,7 +21,7 @@
 
 > 局限性: 这无法绕过 OpenAI 的彻底 IP 禁令
 
-### Compile
+### 编译
 
 > Ubuntu机器为例:
 
@@ -58,13 +58,15 @@ docker run --rm -it -p 7999:7999 --hostname=opengpt \
   gngpp/opengpt:latest opengpt serve
 ```
 
+### OpenWrt(dev)
+
 ### Command Line(dev)
 
 ### Http Server
 
-- Comes with original ChatGPT WebUI
-- Support unofficial/official API, forward to proxy
-- The API prefix is the same as the official one, only the host name is changed
+- 附带原始 ChatGPT WebUI
+- 支持非官方/官方API，转发至代理
+- API前缀与官方一致，仅更改主机名
 
 - API文档
   - Platfrom API [doc](https://platform.openai.com/docs/api-reference)
