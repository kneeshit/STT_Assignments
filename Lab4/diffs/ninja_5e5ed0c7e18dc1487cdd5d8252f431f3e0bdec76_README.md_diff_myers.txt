diff --git a/README.md b/README.md
index b2c4199..f56d6c5 100644
--- a/README.md
+++ b/README.md
@@ -1,4 +1,4 @@
-<br>简体中文 | [English](README_en.md)
+<br>English | [简体中文](README_zh.md)
 
 [![CI](https://github.com/gngpp/ninja/actions/workflows/CI.yml/badge.svg)](https://github.com/gngpp/ninja/actions/workflows/CI.yml)
 [![CI](https://github.com/gngpp/ninja/actions/workflows/Release.yml/badge.svg)](https://github.com/gngpp/ninja/actions/workflows/Release.yml)
@@ -15,45 +15,45 @@
 
 # ninja
 
-逆向工程的 `ChatGPT` 代理（绕过 Cloudflare 403 Access Denied）
+Reverse engineered `ChatGPT` proxy (bypass Cloudflare 403 Access Denied)
 
-### 功能
+### Features
 
-- API密钥获取
-- 电子邮件/密码帐户认证 (暂时不支持Google/Microsoft第三方登录)
-- `Unofficial`/`Official`/`ChatGPT-to-API` Http API 代理 (供第三方客户端接入)
-- 支持代理池
-- 极少的内存占用
-- 附带的ChatGPT WebUI
+- API key acquisition
+- Email/password account authentication (Google/Microsoft third-party login is temporarily not supported)
+- `Unofficial`/`Official`/`ChatGPT-to-API` Http API proxy (for third-party client access)
+- Support IP proxy pool
+- Minimal memory usage
+- ChatGPT WebUI
 
-> 局限性: 无法绕过 OpenAI 的彻底 IP 禁令
+> Limitations: This cannot bypass OpenAI's outright IP ban
 
-### 绕过IP限制
+### Bypass IP restrictions
 
-这里`IP限制`是指`OpenAI`对`单IP`请求速率限制，你需要了解什么是`puid`，默认请求models接口返回`puid cookie`。
-另外，`GPT-4`会话必须带上`puid`发送，在使用第三方客户端发送`GPT-4`会话时可能不会保存也不会获取`puid`，你需要在服务端处理:
+Here `IP limit` refers to `OpenAI`'s request rate limit for `single IP`. You need to understand what `puid` is. The default request models interface returns `puid cookie`.
+In addition, the `GPT-4` session must be sent with `puid`. When using a third-party client to send a `GPT-4` conversation, the `puid` may not be saved or obtained. You need to handle it on the server side:
 
-- 使用启动参数`--puid`单独设置共享使用，此方式不支持更新
-- 使用启动参数`--puid-user`，设置`Account Plus`账号来获取`puid`，并且会定时更新
+- Use the startup parameter `--puid` to set up shared use separately. This method does not support updates.
+- Use the startup parameter `--puid-user` to set the `Account Plus` account to obtain the `puid`, and it will be updated regularly
 
 ### ArkoseLabs
 
-发送`GPT4`对话需要`Arkose Token`作为参数发送，支持的解决方案暂时只有三种
+Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter, and there are only three supported solutions for the time being
 
-1) 获取`Arkose Token`的端点，不管你用什么方式，使用 `--arkose-token-endpoint` 指定端点获取token，支持的`JSON`格式，一般按照社区的格式：`{"token":"xxxxxx"}`
+1) The endpoint obtained by `Arkose Token`, no matter what method you use, use `--arkose-token-endpoint` to specify the endpoint to obtain the token. The supported `JSON` format is generally in accordance with the format of the community: `{"token": "xxxxxx"}`
 
-2) 使用HAR，`ChatGPT` 官网发送一次 `GPT4` 会话消息，浏览器 `F12` 下载 `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` 接口的HAR日志记录文件，使用启动参数 `--arkose-har-file` 指定HAR文件路径使用（不指定路径则使用默认路径`~/chat.openai.com.har`，可直接上传更新HAR），支持上传更新HAR，请求路径:`/har/upload`，可选上传身份验证参数:`--arkose-har-upload-key`
+2) Using HAR, `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97- 6ADB7EFF8147` For the HAR log file of the interface, use the startup parameter `--arkose-har-file` to specify the HAR file path to use (if the path is not specified, the default path `~/chat.openai.com.har` will be used, and updates can be uploaded directly HAR), supports uploading and updating HAR, request path: `/har/upload`, optional upload authentication parameter: `--arkose-har-upload-key`
 
-3) 使用[YesCaptcha](https://yescaptcha.com/i/1Cc5i4) / [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d)平台进行验证码解析，启动参数`--arkose-solver`选择平台（默认使用`YesCaptcha`），`--arkose-solver-key` 填写`Client Key`
+3) Use [YesCaptcha](https://yescaptcha.com/i/1Cc5i4)/[CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d) platform for verification code parsing, start the parameter `--arkose-solver` to select the platform (the default is `YesCaptcha`), `--arkose-solver-key` fill in `Client Key`
 
-- 三种方案都使用，优先级是：`HAR` > `YesCaptcha` / `CapSolver` > `Arkose Token 端点`
-- `YesCaptcha` / `CapSolver`推荐搭配HAR使用，出验证码则调用解析器处理，验证后HAR使用更持久
+- All three solutions are used, the priority is: `HAR` > `YesCaptcha/CapSolver` > `Arkose Token endpoint`
+- `YesCaptcha/CapSolver` is recommended to be used with HAR. When the verification code is generated, the parser is called for processing. After verification, HAR is more durable.
 
 ### Command Line(dev)
 
-### Http 服务
+### Http Server
 
-#### 公开接口, `*` 表示任意`URL`后缀
+#### Public interface, `*` represents any `URL` suffix
 
 - backend-api, <https://host:port/backend-api/*>
 - public-api, <https://host:port/public-api/*>
@@ -61,39 +61,40 @@
 - dashboard-api, <https://host:port/dashboard/*>
 - chatgpt-to-api, <https://host:port/to/v1/chat/completions>
 
-#### API文档
+#### API documentation
 
 - Platfrom API [doc](https://platform.openai.com/docs/api-reference)
 - Backend API [doc](doc/rest.http)
 
-> 关于关于`ChatGPT`转`API`使用，直接拿`AceessToken`当`API Key`使用，接口路径：`/to/v1/chat/completions`
+> About using `ChatGPT` to `API`, use `AceessToken` directly as `API Key`, interface path: `/to/v1/chat/completions`
 
-#### 基本服务
+#### Basic services
 
-- 原汁原味ChatGPT WebUI
-- 公开`非官方`/`官方API`代理
-- `API`前缀与官方一致
-- `ChatGPT` 转 `API`
-- 可接入第三方客户端
-- 可接入IP代理池，提高并发
+- Authentic ChatGPT WebUI
+- Expose `unofficial`/`official API` proxies
+- The `API` prefix is consistent with the official
+- `ChatGPT` To `API`
+- Accessible to third-party clients
+- Access to IP proxy pool to improve concurrency
+- API documentation
 
-- 参数说明
-  - `--level`，环境变量 `LOG`，日志级别: 默认info
-  - `--host`，环境变量 `HOST`， 服务监听地址: 默认0.0.0.0，
-  - `--port`，环境变量 `PORT`， 监听端口: 默认7999
-  - `--tls-cert`，环境变量 `TLS_CERT`，TLS证书公钥，支持格式: EC/PKCS8/RSA
-  - `--tls-key`，环境变量 `TLS_KEY`，TLS证书私钥
-  - `--proxies`，代理，支持代理池，多个代理使用`,`隔开，格式: protocol://user:pass@ip:port，如果本地IP被Ban，使用代理池时需要关闭直连IP使用，`--disable-direct`关闭直连，否则会根据负载均衡使用你被Ban的本地IP
-  - `--workers`， 工作线程: 默认1
-  - `--disable-webui`, 如果不想使用默认自带的WebUI，使用此参数关闭
+- Parameter Description
+  - `--level`, environment variable `LOG`, log level: default info
+  - `--host`, environment variable `HOST`, service listening address: default 0.0.0.0,
+  - `--port`, environment variable `PORT`, listening port: default 7999
+  - `--tls-cert`, environment variable `TLS_CERT`', TLS certificate public key. Supported format: EC/PKCS8/RSA
+  - `--tls-key`, environment variable `TLS_KEY`, TLS certificate private key
+  - `--proxies`, Proxy, supports proxy pool, multiple proxies are separated by `,`, format: protocol://user:pass@ip:port, if the local IP is banned, you need to turn off the use of direct IP when using the proxy pool, `-- disable-direct` turns off direct connection, otherwise your banned local IP will be used according to load balancing
+  - `--workers`, worker threads: default 1
+  - `--disable-webui`, if you don’t want to use the default built-in WebUI, use this parameter to turn it off
 
-[...](https://github.com/gngpp/ninja/blob/main/README_zh.md#%E5%91%BD%E4%BB%A4%E6%89%8B%E5%86%8C)
+[...](https://github.com/gngpp/ninja/blob/main/README.md#command-manual)
 
-### 安装
+### Install
 
 - #### Ubuntu(Other Linux)
 
-  GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
+Making [Releases](https://github.com/gngpp/ninja/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
 wget https://github.com/gngpp/ninja/releases/download/v0.5.6/ninja-0.5.6-x86_64-unknown-linux-musl.deb
@@ -103,7 +104,7 @@ ninja serve run
 
 - #### OpenWrt
 
-GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
+There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/ninja/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
 ```shell
 wget https://github.com/gngpp/ninja/releases/download/v0.5.6/ninja_0.5.6_aarch64_generic.ipk
@@ -126,7 +127,7 @@ docker run --rm -it -p 7999:7999 --name=ninja \
 
 - Docker Compose
 
-> `CloudFlare Warp`你的地区不支持（China）请把它删掉，或者你的`VPS`IP可直连`OpenAI`，那么也可以删掉
+> `CloudFlare Warp` is not supported in your region (China), please delete it, or if your `VPS` IP can be directly connected to `OpenAI`, you can also delete it
 
 ```yaml
 version: '3'
@@ -168,7 +169,7 @@ services:
 
 ```
 
-### 命令手册
+### Command Manual
 
 ```shell
 $ ninja serve --help
@@ -245,7 +246,7 @@ Options:
           Print help
 ```
 
-### 平台支持
+### Platform Support
 
 - Linux
   - `x86_64-unknown-linux-musl`
@@ -261,22 +262,25 @@ Options:
   - `x86_64-apple-darwin`
   - `aarch64-apple-darwin`
 
-### 编译
+### Compile
 
-- Linux编译，Ubuntu机器为例:
+- Linux compile, Ubuntu machine for example:
 
 ```shell
-# 本机编译
+
+sudo apt update -y && sudo apt install rename
+
+# Native compilation
 git clone https://github.com/gngpp/ninja.git && cd ninja
 ./build.sh
 
-# 跨平台编译，依赖于docker(如果您可以自己解决跨平台编译依赖)，默认使用docker构建linux/windows平台
+# Cross-platform compilation, relying on docker (if you can solve cross-platform compilation dependencies on your own)
+# Default using docker build linux/windows platform 
 ./build_cross.sh
-
-# 默认在Macos上构建Macos平台
+# The MacOS platform is built on MacOS by default
 os=macos ./build_cross.sh 
 
-# 编译单个平台二进制，以 aarch64-unknown-linux-musl 为例:
+# Compile a single platform binary, take aarch64-unknown-linux-musl as an example: 
 docker run --rm -it --user=$UID:$(id -g $USER) \
   -v $(pwd):/home/rust/src \
   -v $HOME/.cargo/registry:/root/.cargo/registry \
@@ -285,7 +289,7 @@ docker run --rm -it --user=$UID:$(id -g $USER) \
   cargo build --release
 ```
 
-- OpenWrt 编译
+- OpenWrt Compile
 
 ```shell
 cd package
@@ -295,7 +299,7 @@ make menuconfig # choose LUCI->Applications->luci-app-ninja
 make V=s
 ```
 
-### 预览
+### Preview
 
 ![img0](./doc/img/img0.png)
 ![img1](./doc/img/img1.png)
