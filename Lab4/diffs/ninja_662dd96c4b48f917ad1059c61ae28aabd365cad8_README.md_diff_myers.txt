diff --git a/README.md b/README.md
index 0aad1d4..09945ad 100644
--- a/README.md
+++ b/README.md
@@ -218,7 +218,7 @@ Options:
       --tb-store-strategy <TB_STORE_STRATEGY>
           Token bucket store strategy (mem/redis) [env: OPENGPT_TB_STORE_STRATEGY=] [default: mem]
       --tb-redis-url <TB_REDIS_URL>
-          Token bucket redis url(support cluster), Example: redis://user:pass@ip:port [env: OPENGPT_TB_REDIS_URL=] [default: redis://127.0.0.1:6379]
+          Token bucket redis url, Example: redis://user:pass@ip:port [env: OPENGPT_TB_REDIS_URL=] [default: redis://127.0.0.1:6379]
       --tb-capacity <TB_CAPACITY>
           Token bucket capacity [env: OPENGPT_TB_CAPACITY=] [default: 60]
       --tb-fill-rate <TB_FILL_RATE>
