diff --git a/README.md b/README.md
index b06a8c3..a968056 100644
--- a/README.md
+++ b/README.md
@@ -39,6 +39,8 @@ Options:
           Server Listen port [env: OPENGPT_PORT=] [default: 7999]
   -W, --workers <WORKERS>
           Server worker-pool size (Recommended number of CPU cores) [env: OPENGPT_WORKERS=] [default: 1]
+  -L, --level <LEVEL>
+          Log level (info/debug/warn/trace/error) [env: OPENGPT_LOG_LEVEL=] [default: info]
       --proxy <PROXY>
           Server proxy, example: protocol://user:pass@ip:port [env: OPENGPT_PROXY=]
       --tcp-keepalive <TCP_KEEPALIVE>
