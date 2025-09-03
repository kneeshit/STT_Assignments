diff --git a/README_zh.md b/README_zh.md
index 40713fe..9bcafa9 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -162,10 +162,10 @@ opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
   - `--level`，环境变量 `OPENGPT_LOG_LEVEL`，日志级别: 默认info
   - `--host`，环境变量 `OPENGPT_HOST`， 服务监听地址: 默认0.0.0.0，
   - `--port`，环境变量 `OPENGPT_PORT`， 监听端口: 默认7999
-  - `--workers`，环境变量 `OPENGPT_WORKERS`， 工作线程: 默认1
   - `--tls-cert`，环境变量 `OPENGPT_TLS_CERT`，TLS证书公钥，支持格式: EC/PKCS8/RSA
   - `--tls-key`，环境变量 `OPENGPT_TLS_KEY`，TLS证书私钥
-  - `--proxies`，环境变量 `OPENGPT_PROXY`，代理，支持代理池，格式: protocol://user:pass@ip:port
+  - `--proxies`，代理，支持代理池，格式: protocol://user:pass@ip:port
+  - `--workers`， 工作线程: 默认1
 
 ...
 
@@ -177,7 +177,7 @@ Usage: opengpt serve run [OPTIONS]
 
 Options:
   -C, --config <CONFIG>
-          Configuration file path (toml format file) [env: OPENGPT_CONFIG=]
+          Configuration file path (toml format file)
   -H, --host <HOST>
           Server Listen host [env: OPENGPT_HOST=] [default: 0.0.0.0]
   -L, --level <LEVEL>
@@ -185,17 +185,17 @@ Options:
   -P, --port <PORT>
           Server Listen port [env: OPENGPT_PORT=] [default: 7999]
   -W, --workers <WORKERS>
-          Server worker-pool size (Recommended number of CPU cores) [env: OPENGPT_WORKERS=] [default: 1]
+          Server worker-pool size (Recommended number of CPU cores) [default: 1]
       --concurrent-limit <CONCURRENT_LIMIT>
-          Concurrent limit (Enforces a limit on the concurrent number of requests the underlying) [env: OPENGPT_CONCUURENT_LIMIT=] [default: 65535]
+          Enforces a limit on the concurrent number of requests the underlying [default: 65535]
       --proxies <PROXIES>
-          Server proxies pool, Example: protocol://user:pass@ip:port [env: OPENGPT_PROXY=]
+          Server proxies pool, Example: protocol://user:pass@ip:port
       --timeout <TIMEOUT>
-          Client timeout (seconds) [env: OPENGPT_TIMEOUT=] [default: 600]
+          Client timeout (seconds) [default: 600]
       --connect-timeout <CONNECT_TIMEOUT>
-          Client connect timeout (seconds) [env: OPENGPT_CONNECT_TIMEOUT=] [default: 60]
+          Client connect timeout (seconds) [default: 60]
       --tcp-keepalive <TCP_KEEPALIVE>
-          TCP keepalive (seconds) [env: OPENGPT_TCP_KEEPALIVE=] [default: 60]
+          TCP keepalive (seconds) [default: 60]
       --tls-cert <TLS_CERT>
           TLS certificate file path [env: OPENGPT_TLS_CERT=]
       --tls-key <TLS_KEY>
@@ -203,33 +203,33 @@ Options:
       --puid <PUID>
           PUID cookie value of Plus account [env: OPENGPT_PUID=]
       --puid-user <PUID_USER>
-          Obtain the PUID of the Plus account user. Supports split: ':', '-', '--' ... , Example: `user:pass` or `user:pass:mfa` [env: OPENGPT_PUID_USER=]
+          Obtain the PUID of the Plus account user, Example: `user:pass` or `user:pass:mfa`
       --api-prefix <API_PREFIX>
           Web UI api prefix [env: OPENGPT_UI_API_PREFIX=]
       --arkose-endpoint <ARKOSE_ENDPOINT>
-          Arkose endpoint, Example: https://client-api.arkoselabs.com [env: OPENGPT_ARKOSE_ENDPOINT=]
+          Arkose endpoint, Example: https://client-api.arkoselabs.com
   -A, --arkose-token-endpoint <ARKOSE_TOKEN_ENDPOINT>
-          Get arkose-token endpoint [env: OPENGPT_ARKOSE_TOKEN_ENDPOINT=]
-      --arkose-yescaptcha-key <ARKOSE_YESCAPTCHA_KEY>
-          yescaptcha client key [env: OPENGPT_ARKOSE_YESCAPTCHA_KEY=]
+          Get arkose-token endpoint
+  -Y, --arkose-yescaptcha-key <ARKOSE_YESCAPTCHA_KEY>
+          yescaptcha client key
   -S, --sign-secret-key <SIGN_SECRET_KEY>
-          Enable url signature (signature secret key) [env: OPENGPT_SIGNATURE=]
+          Enable url signature (signature secret key)
   -T, --tb-enable
-          Enable token bucket flow limitation [env: OPENGPT_TB_ENABLE=]
+          Enable token bucket flow limitation
       --tb-store-strategy <TB_STORE_STRATEGY>
-          Token bucket store strategy (mem/redis) [env: OPENGPT_TB_STORE_STRATEGY=] [default: mem]
+          Token bucket store strategy (mem/redis) [default: mem]
       --tb-redis-url <TB_REDIS_URL>
-          Token bucket redis url, Example: redis://user:pass@ip:port [env: OPENGPT_TB_REDIS_URL=] [default: redis://127.0.0.1:6379]
+          Token bucket redis url, Example: redis://user:pass@ip:port [default: redis://127.0.0.1:6379]
       --tb-capacity <TB_CAPACITY>
-          Token bucket capacity [env: OPENGPT_TB_CAPACITY=] [default: 60]
+          Token bucket capacity [default: 60]
       --tb-fill-rate <TB_FILL_RATE>
-          Token bucket fill rate [env: OPENGPT_TB_FILL_RATE=] [default: 1]
+          Token bucket fill rate [default: 1]
       --tb-expired <TB_EXPIRED>
-          Token bucket expired (seconds) [env: OPENGPT_TB_EXPIRED=] [default: 86400]
+          Token bucket expired (seconds) [default: 86400]
       --cf-site-key <CF_SITE_KEY>
-          Cloudflare turnstile captcha site key [env: OPENGPT_CF_SITE_KEY=]
+          Cloudflare turnstile captcha site key
       --cf-secret-key <CF_SECRET_KEY>
-          Cloudflare turnstile captcha secret key [env: OPENGPT_CF_SECRET_KEY=]
+          Cloudflare turnstile captcha secret key
   -D, --disable-webui
           Disable WebUI [env: OPENGPT_DISABLE_WEBUI=]
   -h, --help
