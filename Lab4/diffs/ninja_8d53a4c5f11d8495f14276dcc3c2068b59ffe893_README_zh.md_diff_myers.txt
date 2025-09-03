diff --git a/README_zh.md b/README_zh.md
index 60296d3..0f71918 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -97,8 +97,8 @@
   GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.6.7/ninja-0.6.7-x86_64-unknown-linux-musl.deb
-dpkg -i ninja-0.6.7-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.6.8/ninja-0.6.8-x86_64-unknown-linux-musl.deb
+dpkg -i ninja-0.6.8-x86_64-unknown-linux-musl.deb
 ninja serve run
 ```
 
@@ -107,11 +107,11 @@ ninja serve run
 GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.6.7/ninja_0.6.7_aarch64_generic.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.6.7/luci-app-ninja_1.1.3-1_all.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.6.7/luci-i18n-ninja-zh-cn_1.1.3-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.8/ninja_0.6.8_aarch64_generic.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.8/luci-app-ninja_1.1.3-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.8/luci-i18n-ninja-zh-cn_1.1.3-1_all.ipk
 
-opkg install ninja_0.6.7_aarch64_generic.ipk
+opkg install ninja_0.6.8_aarch64_generic.ipk
 opkg install luci-app-ninja_1.1.3-1_all.ipk
 opkg install luci-i18n-ninja-zh-cn_1.1.3-1_all.ipk
 ```
@@ -192,6 +192,10 @@ Options:
           Enforces a limit on the concurrent number of requests the underlying [default: 65535]
   -x, --proxies <PROXIES>
           Server proxies pool, Example: protocol://user:pass@ip:port [env: PROXIES=]
+  -i, --interface <INTERFACE>
+          Bind address for outgoing connections [env: INTERFACE=]
+  -I, --ipv6-subnet <IPV6_SUBNET>
+          IPv6 subnet, Example: 2001:19f0:6001:48e4::/64 [env: IPV4_SUBNET=]
       --disable-direct
           Disable direct connection [env: DISABLE_DIRECT=]
       --cookie-store
@@ -202,6 +206,8 @@ Options:
           Client connect timeout (seconds) [default: 60]
       --tcp-keepalive <TCP_KEEPALIVE>
           TCP keepalive (seconds) [default: 60]
+      --pool-idle-timeout <POOL_IDLE_TIMEOUT>
+          Set an optional timeout for idle sockets being kept-alive [default: 90]
       --tls-cert <TLS_CERT>
           TLS certificate file path [env: TLS_CERT=]
       --tls-key <TLS_KEY>
@@ -212,6 +218,12 @@ Options:
           WebUI api prefix [env: API_PREFIX=]
       --preauth-api <PREAUTH_API>
           PreAuth Cookie API URL [env: PREAUTH_API=] [default: https://ai.fakeopen.com/auth/preauth]
+  -D, --disable-webui
+          Disable WebUI [env: DISABLE_WEBUI=]
+      --cf-site-key <CF_SITE_KEY>
+          Cloudflare turnstile captcha site key [env: CF_SECRET_KEY=]
+      --cf-secret-key <CF_SECRET_KEY>
+          Cloudflare turnstile captcha secret key [env: CF_SITE_KEY=]
       --arkose-endpoint <ARKOSE_ENDPOINT>
           Arkose endpoint, Example: https://client-api.arkoselabs.com
   -A, --arkose-token-endpoint <ARKOSE_TOKEN_ENDPOINT>
@@ -240,12 +252,6 @@ Options:
           Token bucket fill rate [default: 1]
       --tb-expired <TB_EXPIRED>
           Token bucket expired (seconds) [default: 86400]
-      --cf-site-key <CF_SITE_KEY>
-          Cloudflare turnstile captcha site key [env: CF_SECRET_KEY=]
-      --cf-secret-key <CF_SECRET_KEY>
-          Cloudflare turnstile captcha secret key [env: CF_SITE_KEY=]
-  -D, --disable-webui
-          Disable WebUI [env: DISABLE_WEBUI=]
   -h, --help
           Print help
 ```
