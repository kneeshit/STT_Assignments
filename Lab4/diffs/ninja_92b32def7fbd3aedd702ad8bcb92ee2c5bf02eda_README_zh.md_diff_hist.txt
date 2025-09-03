diff --git a/README_zh.md b/README_zh.md
index 5a053e9..2247736 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -22,6 +22,7 @@
 - API密钥获取
 - 电子邮件/密码帐户认证 (由于作者没有账号，暂不支持Google/微软第三方登录)
 - Unofficial/Official Http API 代理 (供第三方客户端接入)
+- ChatGPT to API
 - 原汁原味的ChatGPT WebUI
 - 极少的内存占用
 
@@ -138,14 +139,25 @@ opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
 ### Http 服务
 
+> 公开接口, `*` 表示任意`URL`后缀
+>
+> - backend-api, <https://host:port/backend-api/*>
+> - public-api, <https://host:port/public-api/*>
+> - platform-api, <https://host:port/v1/*>
+> - dashboard-api, <https://host:port/dashboard/*>
+> - chatgpt-to-api, <https://host:port/conv/v1/chat/completions>
+>
+> 详细API文档
+>
+> - Platfrom API [doc](https://platform.openai.com/docs/api-reference)
+> - Backend API [doc](doc/rest.http)
+
 - 原汁原味ChatGPT WebUI
-- 支持非官方/官方API代理
-- API前缀与官方一致
+- 公开`非官方`/`官方API`代理
+- `API`前缀与官方一致
+- `ChatGPT` 转 `API`
 - 可接入第三方客户端
-- 可接入IP代理池，提高并发量
-- API文档
-  - Platfrom API [doc](https://platform.openai.com/docs/api-reference)
-  - Backend API [doc](doc/rest.http)
+- 可接入IP代理池，提高并发
 
 - 参数说明
   - `--level`，环境变量 `OPENGPT_LOG_LEVEL`，日志级别: 默认info
@@ -156,6 +168,8 @@ opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
   - `--tls-key`，环境变量 `OPENGPT_TLS_KEY`，TLS证书私钥
   - `--proxies`，环境变量 `OPENGPT_PROXY`，代理，支持代理池，格式: protocol://user:pass@ip:port
 
+...
+
 ```shell
 $ opengpt serve --help
 Start the http server
@@ -210,9 +224,11 @@ Options:
 git clone https://github.com/gngpp/opengpt.git && cd opengpt
 ./build.sh
 
-# 跨平台编译，依赖于docker(如果您可以自己解决跨平台编译依赖)，编译所有支持平台
-./build_cross.sh # 默认使用docker构建linux/windows平台
-os=macos ./build_cross.sh # 默认在Macos上构建Macos平台
+# 跨平台编译，依赖于docker(如果您可以自己解决跨平台编译依赖)，默认使用docker构建linux/windows平台
+./build_cross.sh 
+
+# 默认在Macos上构建Macos平台
+os=macos ./build_cross.sh
 
 # 编译单个平台二进制，以 aarch64-unknown-linux-musl 为例:
 docker run --rm -it --user=$UID:$(id -g $USER) \
