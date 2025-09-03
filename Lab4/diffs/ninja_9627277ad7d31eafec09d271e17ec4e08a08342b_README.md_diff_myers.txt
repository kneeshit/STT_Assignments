diff --git a/README.md b/README.md
index 6cf6441..80d4e43 100644
--- a/README.md
+++ b/README.md
@@ -47,6 +47,8 @@ Options:
           Enable url signature (signature secret key) [env: OPENGPT_SIGNATURE=]
   -T, --tb-enable
           Enable token bucket flow limitation [env: OPENGPT_TB_ENABLE=]
+      --tb-store-strategy <TB_STORE_STRATEGY>
+          Token bucket store strategy (mem/redis) [env: OPENGPT_TB_STORE_STRATEGY=] [default: mem]
       --tb-capacity <TB_CAPACITY>
           Token bucket capacity [env: OPENGPT_TB_CAPACITY=] [default: 60]
       --tb-fill-rate <TB_FILL_RATE>
