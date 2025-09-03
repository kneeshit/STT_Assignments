diff --git a/README_zh.md b/README_zh.md
index e123fe1..7d63a33 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -17,62 +17,63 @@
 
 逆向工程的 `ChatGPT` 代理（绕过 Cloudflare 403 Access Denied）
 
-### 功能
+### 特征
 
 - API密钥获取
-- 电子邮件/密码帐户认证 (暂时不支持Google/Microsoft第三方登录)
-- `Unofficial`/`Official`/`ChatGPT-to-API` Http API 代理 (供第三方客户端接入)
-- 支持IP代理池
-- 极少的内存占用
+- 电子邮件/密码帐户认证 (不支持Google/Microsoft第三方登录)
+- `ChatGPT-API`/`OpenAI-API`/`ChatGPT-to-API` Http API 代理 (供第三方客户端接入)
+- 支持IP代理池（支持使用Ipv6子网作为代理池）
 - ChatGPT WebUI
+- 极少的内存占用
 
 > 局限性: 无法绕过 OpenAI 的彻底 IP 禁令
 
-
 ### ArkoseLabs
 
-发送`GPT4`对话需要`Arkose Token`作为参数发送，支持的解决方案暂时只有三种
+发送`GPT4/GPT-3.5(已经灰度)`对话需要`Arkose Token`作为参数发送，支持的解决方案暂时只有三种
 
-1) 获取`Arkose Token`的端点，不管你用什么方式，使用 `--arkose-token-endpoint` 指定端点获取token，支持的`JSON`格式，一般按照社区的格式：`{"token":"xxxxxx"}`
+1) 使用HAR，`ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-chat4-har-file` 指定HAR文件路径使用（不指定路径则使用默认路径`~/.chat4.openai.com.har`，可直接上传更新HAR），支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
 
-2) 使用HAR，`ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-chat-har-file` 指定HAR文件路径使用（不指定路径则使用默认路径`~/.chat.openai.com.har`，可直接上传更新HAR），支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
-
-3) 使用[YesCaptcha](https://yescaptcha.com/i/1Cc5i4) / [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d)平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
+2) 使用[YesCaptcha](https://yescaptcha.com/i/1Cc5i4) / [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d)平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
 
 - 三种方案都使用，优先级是：`HAR` > `YesCaptcha` / `CapSolver` > `Arkose Token 端点`
 - `YesCaptcha` / `CapSolver`推荐搭配HAR使用，出验证码则调用解析器处理，验证后HAR使用更持久
 
 > 目前OpenAI已经更新登录需要验证`Arkose Token`，解决方式同GPT4，填写启动参数指定HAR文件`--arkose-auth-har-file`。不想上传，可以通过浏览器打码登录，非必需。
 
-### Command Line(dev)
-
 ### Http 服务
 
 #### 公开接口, `*` 表示任意`URL`后缀
 
-- backend-api, <https://host:port/backend-api/*>
-- public-api, <https://host:port/public-api/*>
-- platform-api, <https://host:port/v1/*>
-- dashboard-api, <https://host:port/dashboard/*>
-- chatgpt-to-api, <https://host:port/to/v1/chat/completions>
+- ChatGPT-API
+  - <https://host:port/public-api/*>
+  - <https://host:port/backend-api/*>
+  
+- OpenAI-API
+  - <https://host:port/v1/*>
+
+- Platform-API
+  - <https://host:port/dashboard/*>
+- ChatGPT-To-API
+  - <https://host:port/to/v1/chat/completions>
+  > 关于`ChatGPT`转`API`使用方法，`AceessToken`当`API Key`使用
 
 #### API文档
 
 - Platfrom API [doc](https://platform.openai.com/docs/api-reference)
 - Backend API [doc](doc/rest.http)
 
-> 关于关于`ChatGPT`转`API`使用，直接拿`AceessToken`当`API Key`使用，接口路径：`/to/v1/chat/completions`
-
 #### 基本服务
 
-- 原汁原味ChatGPT WebUI
-- 公开`非官方`/`官方API`代理
+- ChatGPT WebUI
+- 公开`ChatGPT-API`/`OpenAI-API`代理
 - `API`前缀与官方一致
 - `ChatGPT` 转 `API`
 - 可接入第三方客户端
 - 可接入IP代理池，提高并发
 
-- 参数说明
+#### 参数说明
+
 - `--level`，环境变量 `LOG`，日志级别: 默认info
 - `--bind`，环境变量 `BIND`， 服务监听地址: 默认0.0.0.0:7999，
 - `--tls-cert`，环境变量 `TLS_CERT`，TLS证书公钥，支持格式: EC/PKCS8/RSA
@@ -101,12 +102,12 @@ GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编
 
 ```shell
 wget https://github.com/gngpp/ninja/releases/download/v0.7.2/ninja_0.7.2_aarch64_generic.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.7.2/luci-app-ninja_1.1.3-1_all.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.7.2/luci-i18n-ninja-zh-cn_1.1.3-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.7.2/luci-app-ninja_1.1.4-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.7.2/luci-i18n-ninja-zh-cn_1.1.4-1_all.ipk
 
 opkg install ninja_0.7.2_aarch64_generic.ipk
-opkg install luci-app-ninja_1.1.3-1_all.ipk
-opkg install luci-i18n-ninja-zh-cn_1.1.3-1_all.ipk
+opkg install luci-app-ninja_1.1.4-1_all.ipk
+opkg install luci-i18n-ninja-zh-cn_1.1.4-1_all.ipk
 ```
 
 - #### Docker
