diff --git a/README_zh.md b/README_zh.md
index 8180647..f81d63c 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -50,8 +50,8 @@
   GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.5/opengpt-0.3.5-x86_64-unknown-linux-musl.deb
-dpkg -i opengpt-0.3.5-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.6/opengpt-0.3.6-x86_64-unknown-linux-musl.deb
+dpkg -i opengpt-0.3.6-x86_64-unknown-linux-musl.deb
 opengpt serve run
 ```
 
@@ -125,11 +125,11 @@ services:
 GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.5/opengpt_0.3.5_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.5/luci-app-opengpt_1.0.2-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.3.5/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.6/opengpt_0.3.6_aarch64_generic.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.6/luci-app-opengpt_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.3.6/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
-opkg install opengpt_0.3.5_aarch64_generic.ipk
+opkg install opengpt_0.3.6_aarch64_generic.ipk
 opkg install luci-app-opengpt_1.0.2-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 ```
@@ -176,28 +176,52 @@ Start the http server
 Usage: opengpt serve run [OPTIONS]
 
 Options:
+  -C, --config <CONFIG>
+          Configuration file path (toml format file) [env: OPENGPT_CONFIG=]
   -H, --host <HOST>
           Server Listen host [env: OPENGPT_HOST=] [default: 0.0.0.0]
   -P, --port <PORT>
           Server Listen port [env: OPENGPT_PORT=] [default: 7999]
-  -W, --workers <WORKERS>
-          Server worker-pool size (Recommended number of CPU cores) [env: OPENGPT_WORKERS=] [default: 1]
   -L, --level <LEVEL>
           Log level (info/debug/warn/trace/error) [env: OPENGPT_LOG_LEVEL=] [default: info]
+  -W, --workers <WORKERS>
+          Server worker-pool size (Recommended number of CPU cores) [env: OPENGPT_WORKERS=] [default: 1]
+      --concurrent-limit <CONCURRENT_LIMIT>
+          Concurrent limit (Enforces a limit on the concurrent number of requests the underlying) [env: OPENGPT_CONCUURENT_LIMIT=] [default: 65535]
       --proxies <PROXIES>
           Server proxies pool, example: protocol://user:pass@ip:port [env: OPENGPT_PROXY=]
+      --timeout <TIMEOUT>
+          Client timeout (secends) [env: OPENGPT_TIMEOUT=] [default: 600]
+      --connect-timeout <CONNECT_TIMEOUT>
+          Client connect timeout (secends) [env: OPENGPT_CONNECT_TIMEOUT=] [default: 60]
       --tcp-keepalive <TCP_KEEPALIVE>
-          TCP keepalive (second) [env: OPENGPT_TCP_KEEPALIVE=] [default: 5]
+          TCP keepalive (secends) [env: OPENGPT_TCP_KEEPALIVE=] [default: 60]
       --tls-cert <TLS_CERT>
           TLS certificate file path [env: OPENGPT_TLS_CERT=]
       --tls-key <TLS_KEY>
           TLS private key file path (EC/PKCS8/RSA) [env: OPENGPT_TLS_KEY=]
+      --puid <PUID>
+          Account Plus puid cookie value [env: OPENGPT_PUID=]
+      --puid-email <PUID_EMAIL>
+          Get the user mailbox of the PUID [env: OPENGPT_PUID_EMAIL=]
+      --puid-password <PUID_PASSWORD>
+          Get the user password of the PUID [env: OPENGPT_PUID_PASSWORD=]
+      --puid-mfa <PUID_MFA>
+          Get the user mfa code of the PUID [env: OPENGPT_PUID_MFA=]
+      --api-prefix <API_PREFIX>
+          Web UI api prefix [env: OPENGPT_UI_API_PREFIX=]
+      --arkose-endpoint <ARKOSE_ENDPOINT>
+          Arkose endpoint, Example: https://client-api.arkoselabs.com [env: OPENGPT_ARKOSE_ENDPOINT=]
+  -A, --arkose-token-endpoint <ARKOSE_TOKEN_ENDPOINT>
+          Get arkose-token endpoint [env: OPENGPT_ARKOSE_TOKEN_ENDPOINT=]
   -S, --sign-secret-key <SIGN_SECRET_KEY>
           Enable url signature (signature secret key) [env: OPENGPT_SIGNATURE=]
   -T, --tb-enable
           Enable token bucket flow limitation [env: OPENGPT_TB_ENABLE=]
       --tb-store-strategy <TB_STORE_STRATEGY>
           Token bucket store strategy (mem/redis) [env: OPENGPT_TB_STORE_STRATEGY=] [default: mem]
+      --tb-redis-url <TB_REDIS_URL>
+          Token bucket redis url(support cluster), example: redis://user:pass@ip:port [env: OPENGPT_TB_REDIS_URL=] [default: redis://127.0.0.1:6379]
       --tb-capacity <TB_CAPACITY>
           Token bucket capacity [env: OPENGPT_TB_CAPACITY=] [default: 60]
       --tb-fill-rate <TB_FILL_RATE>
