diff --git a/README_zh.md b/README_zh.md
index a79c060..9ef1d4a 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -17,10 +17,13 @@
 
 一个逆向工程的非官方的 `ChatGPT` 代理（绕过 Cloudflare 403 Access Denied）
 
+### 功能
+
 - API密钥获取
 - 电子邮件/密码帐户认证 (由于作者没有账号，暂不支持Google/微软第三方登录)
 - Unofficial/Official Http API 代理 (供第三方客户端接入)
 - 原汁原味的ChatGPT WebUI
+- 极少的内存占用
 
 > 局限性: 无法绕过 OpenAI 的彻底 IP 禁令
 
@@ -47,9 +50,9 @@
   GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.5/opengpt-0.2.5-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/opengpt-0.2.6-x86_64-unknown-linux-musl.deb
 
-dpkg -i opengpt-0.2.5-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.2.6-x86_64-unknown-linux-musl.deb
 
 opengpt serve run
 ```
@@ -68,11 +71,11 @@ docker run --rm -it -p 7999:7999 --hostname=opengpt \
 GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.5/opengpt_0.2.5_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.5/luci-app-opengpt_1.0.2-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.2.5/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/opengpt_0.2.6_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/luci-app-opengpt_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.2.6/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
-opkg install opengpt_0.2.5_aarch64_generic.ipk
+opkg install opengpt_0.2.6_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.2-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 ```
