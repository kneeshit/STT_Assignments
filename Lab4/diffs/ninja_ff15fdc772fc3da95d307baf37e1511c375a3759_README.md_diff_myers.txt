diff --git a/README.md b/README.md
index 41fcd2d..13c1efd 100644
--- a/README.md
+++ b/README.md
@@ -1,4 +1,4 @@
-<br>简体中文 | [English](README_en.md)
+<br>English | [简体中文](README-zh.md)
 
 [![CI](https://github.com/gngpp/opengpt/actions/workflows/CI.yml/badge.svg)](https://github.com/gngpp/opengpt/actions/workflows/CI.yml)
 <a href="/LICENSE">
@@ -13,20 +13,20 @@
 
 # opengpt
 
-不仅仅是非官方的 ChatGPT 代理（绕过 Cloudflare 403 Access Denied）
+Not just an unofficial ChatGPT proxy (bypass Cloudflare 403 Access Denied)
 
-- API密钥获取
-- 电子邮件/密码帐户认证 (由于作者没有账号，暂不支持Google/微软第三方登录)
-- Unofficial/Official Http API 代理 (供第三方客户端接入)
-- 原汁原味的ChatGPT WebUI
+- API key acquisition
+- Email/password account authentication (Google/Microsoft third-party login is not supported for now because the author does not have an account)
+- Unofficial/Official Http API proxy (for third-party client access)
+- The original ChatGPT WebUI
 
-> 局限性: 无法绕过 OpenAI 的彻底 IP 禁令
+> Limitations: This cannot bypass OpenAI's outright IP ban
+
+### Install
 
-### 安装
-  >
   > #### Ubuntu(Other Linux)
 
-  GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
+Making [Releases](https://github.com/gngpp/opengpt/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
 ```shell
 wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/opengpt-0.1.2-x86_64-unknown-linux-musl.deb
@@ -49,7 +49,7 @@ docker run --rm -it -p 7999:7999 --hostname=opengpt \
 
 > #### OpenWrt
 
-GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
+There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
 ```shell
 wget https://github.com/gngpp/opengpt/releases/download/v0.1.2/opengpt_0.1.2_aarch64_generic.ipk
@@ -63,24 +63,24 @@ opkg install luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
 
 ### Command Line(dev)
 
-### Http 服务
+### Http Server
+
+- Comes with original ChatGPT WebUI
+- Support unofficial/official API, forward to proxy
+- The API prefix is the same as the official one, only the host name is changed
 
-- 原汁原味ChatGPT WebUI
-- 支持非官方/官方API代理
-- API前缀与官方一致
-- 可接入第三方客户端
-- API文档
+- Parameter Description
   - Platfrom API [doc](https://platform.openai.com/docs/api-reference)
   - Backend API [doc](doc/rest.http)
 
-- 参数说明
-  - `--host`，环境变量 `OPENGPT_HOST`， 服务监听地址: 默认0.0.0.0，
-  - `--port`，环境变量 `OPENGPT_PORT`， 监听端口: 默认7999
-  - `--workers`，环境变量 `OPENGPT_WORKERS`， 服务线程数: 默认1
-  - `--level`，环境变量 `OPENGPT_LOG_LEVEL`，日志级别: 默认info
-  - `--tls-cert`，环境变量 `OPENGPT_TLS_CERT`，TLS证书公钥，支持格式: EC/PKCS8/RSA
-  - `--tls-key`，环境变量 `OPENGPT_TLS_KEY`，TLS证书私钥
-  - `--proxy`，环境变量 `OPENGPT_PROXY`，代理，格式: protocol://user:pass@ip:port
+- Parameter Description
+  - `--level`, environment variable `OPENGPT_LOG_LEVEL`, log level: default info
+  - `--host`, environment variable `OPENGPT_HOST`, service listening address: default 0.0.0.0,
+  - `--port`, environment variable `OPENGPT_PORT`, listening port: default 7999
+  - `--workers`, environment variable `OPENGPT_WORKERS`, worker threads: default 1
+  - `--tls-cert`, environment variable `OPENGPT_TLS_CERT`', TLS certificate public key. Supported format: EC/PKCS8/RSA
+  - `--tls-key`, environment variable `OPENGPT_TLS_KEY`, TLS certificate private key
+  - `--proxy`, environment variable `OPENGPT_PROXY`, proxy, format: protocol://user:pass@ip:port
 
 ```shell
 $ opengpt serve --help
@@ -121,9 +121,9 @@ Options:
           Print help
 ```
 
-### 自行编译
+### Compile
 
-- Linux musl 目前支持
+- Linux musl current supports
   - `x86_64-unknown-linux-musl`
   - `aarch64-unknown-linux-musl`
   - `armv7-unknown-linux-musleabi`
@@ -132,26 +132,29 @@ Options:
   - `arm-unknown-linux-musleabihf`
   - `armv5te-unknown-linux-musleabi`
 
-- Linux编译，Ubuntu机器为例:
+- Linux compile, Ubuntu machine for example:
 
 ```shell
-# 本机编译
+
+sudo apt update -y && sudo apt install rename
+
+# Native compilation
 git clone https://github.com/gngpp/opengpt.git && cd opengpt
 ./build.sh
 
-# 跨平台编译，依赖于docker(如果您可以自己解决跨平台编译依赖)，编译所有支持平台
+# Cross-platform compilation, relying on docker (if you can solve cross-platform compilation dependencies on your own)
 ./corss-build.sh
 
-# 编译单个平台二进制，以 aarch64-unknown-linux-musl 为例:
+# Compile a single platform binary, take aarch64-unknown-linux-musl as an example: 
 docker run --rm -it \
   -v $(pwd):/home/rust/src \
-  -v $HOME/.cargo/registry:/root/.cargo/registry \  # 如果你希望使用本地缓存
-  -v $HOME/.cargo/git:/root/.cargo/git \  # 如果你希望使用本地缓存
+  -v $HOME/.cargo/registry:/root/.cargo/registry \  # If you want to use local cache
+  -v $HOME/.cargo/git:/root/.cargo/git \  # If you want to use local cache
   ghcr.io/gngpp/opengpt-builder:aarch64-unknown-linux-musl \
   cargo build --release
 ```
 
-- OpenWrt 编译
+- OpenWrt compile
 
 ```shell
 cd package
@@ -161,13 +164,13 @@ make menuconfig # choose LUCI->Applications->luci-app-opengpt
 make V=s
 ```
 
-### 预览
+### Preview
 
 ![img0](./doc/img/img0.png)
 ![img1](./doc/img/img1.png)
 ![img2](./doc/img/img2.png)
 
-### 参考
+### Reference
 
 - <https://github.com/tjardoo/openai-client>
 - <https://github.com/jpopesculian/reqwest-eventsource>
