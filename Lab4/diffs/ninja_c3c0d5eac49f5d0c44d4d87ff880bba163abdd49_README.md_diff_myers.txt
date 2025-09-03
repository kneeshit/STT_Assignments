diff --git a/README.md b/README.md
index f1a50e7..404c8c3 100644
--- a/README.md
+++ b/README.md
@@ -76,7 +76,7 @@ services:
     restart: unless-stopped
     environment:
       - TZ=Asia/Shanghai
-      - OPENGPT_PROXY=socks5://cloudflare-warp:10000
+      - OPENGPT_PROXIES=socks5://cloudflare-warp:10000
       # - OPENGPT_CONFIG=/serve.toml
       # - OPENGPT_PORT=8080
       # - OPENGPT_HOST=0.0.0.0
@@ -176,7 +176,7 @@ Options:
       --concurrent-limit <CONCURRENT_LIMIT>
           Enforces a limit on the concurrent number of requests the underlying [default: 65535]
       --proxies <PROXIES>
-          Server proxies pool, Example: protocol://user:pass@ip:port
+          Server proxies pool, Example: protocol://user:pass@ip:port [env: OPENGPT_PROXIES=]
       --timeout <TIMEOUT>
           Client timeout (seconds) [default: 600]
       --connect-timeout <CONNECT_TIMEOUT>
@@ -196,9 +196,11 @@ Options:
       --arkose-endpoint <ARKOSE_ENDPOINT>
           Arkose endpoint, Example: https://client-api.arkoselabs.com
   -A, --arkose-token-endpoint <ARKOSE_TOKEN_ENDPOINT>
-          Get arkose-token endpoint
+          Get arkose token endpoint
+  -a, --arkose-har-path <ARKOSE_HAR_PATH>
+          About the browser HAR file path requested by ArkoseLabs
   -Y, --arkose-yescaptcha-key <ARKOSE_YESCAPTCHA_KEY>
-          yescaptcha client key
+          About the yescaptcha platform client key solved by ArkoseLabs
   -S, --sign-secret-key <SIGN_SECRET_KEY>
           Enable url signature (signature secret key)
   -T, --tb-enable
@@ -206,7 +208,7 @@ Options:
       --tb-store-strategy <TB_STORE_STRATEGY>
           Token bucket store strategy (mem/redis) [default: mem]
       --tb-redis-url <TB_REDIS_URL>
-          Token bucket redis url [default: redis://127.0.0.1:6379]
+          Token bucket redis url, Example: redis://user:pass@ip:port [default: redis://127.0.0.1:6379]
       --tb-capacity <TB_CAPACITY>
           Token bucket capacity [default: 60]
       --tb-fill-rate <TB_FILL_RATE>
