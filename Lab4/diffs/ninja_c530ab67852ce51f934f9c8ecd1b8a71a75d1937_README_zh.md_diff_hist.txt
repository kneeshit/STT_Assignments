diff --git a/README_zh.md b/README_zh.md
index 847d2c9..93a7422 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -50,8 +50,8 @@
   GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.7/opengpt-0.3.7-x86_64-unknown-linux-musl.deb
-dpkg -i opengpt-0.3.7-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.8/opengpt-0.3.8-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.3.8-x86_64-unknown-linux-musl.deb
 opengpt serve run
 ```
 
@@ -125,11 +125,11 @@ services:
 GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.7/opengpt_0.3.7_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.7/luci-app-opengpt_1.0.2-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.7/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.8/opengpt_0.3.8_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.8/luci-app-opengpt_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.8/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
-opkg install opengpt_0.3.7_aarch64_generic.ipk
+opkg install opengpt_0.3.8_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.2-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 ```
@@ -180,10 +180,10 @@ Options:
           Configuration file path (toml format file) [env: OPENGPT_CONFIG=]
   -H, --host <HOST>
           Server Listen host [env: OPENGPT_HOST=] [default: 0.0.0.0]
-  -P, --port <PORT>
-          Server Listen port [env: OPENGPT_PORT=] [default: 7999]
   -L, --level <LEVEL>
           Log level (info/debug/warn/trace/error) [env: OPENGPT_LOG_LEVEL=] [default: info]
+  -P, --port <PORT>
+          Server Listen port [env: OPENGPT_PORT=] [default: 7999]
   -W, --workers <WORKERS>
           Server worker-pool size (Recommended number of CPU cores) [env: OPENGPT_WORKERS=] [default: 1]
       --concurrent-limit <CONCURRENT_LIMIT>
@@ -191,11 +191,11 @@ Options:
       --proxies <PROXIES>
           Server proxies pool, Example: protocol://user:pass@ip:port [env: OPENGPT_PROXY=]
       --timeout <TIMEOUT>
-          Client timeout (secends) [env: OPENGPT_TIMEOUT=] [default: 600]
+          Client timeout (seconds) [env: OPENGPT_TIMEOUT=] [default: 600]
       --connect-timeout <CONNECT_TIMEOUT>
-          Client connect timeout (secends) [env: OPENGPT_CONNECT_TIMEOUT=] [default: 60]
+          Client connect timeout (seconds) [env: OPENGPT_CONNECT_TIMEOUT=] [default: 60]
       --tcp-keepalive <TCP_KEEPALIVE>
-          TCP keepalive (secends) [env: OPENGPT_TCP_KEEPALIVE=] [default: 60]
+          TCP keepalive (seconds) [env: OPENGPT_TCP_KEEPALIVE=] [default: 60]
       --tls-cert <TLS_CERT>
           TLS certificate file path [env: OPENGPT_TLS_CERT=]
       --tls-key <TLS_KEY>
@@ -203,13 +203,15 @@ Options:
       --puid <PUID>
           PUID cookie value of Plus account [env: OPENGPT_PUID=]
       --puid-user <PUID_USER>
-          Obtain the PUID of the Plus account user, Example: `user:pass` or `user:pass:mfa` [env: OPENGPT_PUID_USER=]
+          Obtain the PUID of the Plus account user. Supports split: ':', '-', '--' ... , Example: `user:pass` or `user:pass:mfa` [env: OPENGPT_PUID_USER=]
       --api-prefix <API_PREFIX>
           Web UI api prefix [env: OPENGPT_UI_API_PREFIX=]
       --arkose-endpoint <ARKOSE_ENDPOINT>
           Arkose endpoint, Example: https://client-api.arkoselabs.com [env: OPENGPT_ARKOSE_ENDPOINT=]
   -A, --arkose-token-endpoint <ARKOSE_TOKEN_ENDPOINT>
           Get arkose-token endpoint [env: OPENGPT_ARKOSE_TOKEN_ENDPOINT=]
+      --arkose-yescaptcha-key <ARKOSE_YESCAPTCHA_KEY>
+          yescaptcha client key [env: OPENGPT_ARKOSE_YESCAPTCHA_KEY=]
   -S, --sign-secret-key <SIGN_SECRET_KEY>
           Enable url signature (signature secret key) [env: OPENGPT_SIGNATURE=]
   -T, --tb-enable
@@ -223,7 +225,7 @@ Options:
       --tb-fill-rate <TB_FILL_RATE>
           Token bucket fill rate [env: OPENGPT_TB_FILL_RATE=] [default: 1]
       --tb-expired <TB_EXPIRED>
-          Token bucket expired (second) [env: OPENGPT_TB_EXPIRED=] [default: 86400]
+          Token bucket expired (seconds) [env: OPENGPT_TB_EXPIRED=] [default: 86400]
       --cf-site-key <CF_SITE_KEY>
           Cloudflare turnstile captcha site key [env: OPENGPT_CF_SITE_KEY=]
       --cf-secret-key <CF_SECRET_KEY>
