diff --git a/README_zh.md b/README_zh.md
index 2e8d226..4945e07 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -44,8 +44,6 @@ opengpt serve
 docker run --rm -it -p 7999:7999 --hostname=opengpt \
   -e OPENGPT_WORKERS=1 \
   -e OPENGPT_LOG_LEVEL=info \
-  -e OPENGPT_TLS_CERT=/path/to/cert \
-  -e OPENGPT_TLS_KEY=/path/to/key \
   gngpp/opengpt:latest serve
 ```
 
