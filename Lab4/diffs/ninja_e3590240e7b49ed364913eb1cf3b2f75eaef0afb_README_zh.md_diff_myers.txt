diff --git a/README_zh.md b/README_zh.md
index c2feaf6..95cdd2a 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -195,10 +195,8 @@ Options:
           Log level (info/debug/warn/trace/error) [env: LOG=] [default: info]
   -C, --config <CONFIG>
           Configuration file path (toml format file) [env: CONFIG=]
-  -H, --host <HOST>
-          Server Listen host [env: HOST=] [default: 0.0.0.0]
-  -P, --port <PORT>
-          Server Listen port [env: PORT=] [default: 7999]
+  -b, --bind <BIND>
+          Server Bind address [env: BIND=] [default: 0.0.0.0:7999]
   -W, --workers <WORKERS>
           Server worker-pool size (Recommended number of CPU cores) [default: 1]
       --concurrent-limit <CONCURRENT_LIMIT>
@@ -267,6 +265,14 @@ Options:
           Token bucket fill rate [default: 1]
       --tb-expired <TB_EXPIRED>
           Token bucket expired (seconds) [default: 86400]
+  -B, --preauth-bind <PREAUTH_BIND>
+          Preauth MITM server bind address [env: PREAUTH_BIND=] [default: 0.0.0.0:8000]
+  -X, --preauth-upstream <PREAUTH_UPSTREAM>
+          Preauth MITM server upstream proxy [env: PREAUTH_UPSTREAM=]
+      --preauth-cert <PREAUTH_CERT>
+          Preauth MITM server CA certificate file path [default: ca/cert.crt]
+      --preauth-key <PREAUTH_KEY>
+          Preauth MITM server CA private key file path [default: ca/key.pem]
   -h, --help
           Print help
 ```
