diff --git a/README.md b/README.md
index 5cdfcc7..60d2a40 100644
--- a/README.md
+++ b/README.md
@@ -84,7 +84,7 @@ opkg install luci-i18n-opengpt-zh-cn_1.0.6-1_all.ipk
 > #### Docker
 
 ```shell
-docker run --rm -it -p 7999:7999 --hostname=opengpt \
+docker run --rm -it -p 7999:7999 --name=opengpt \
   -e OPENGPT_WORKERS=1 \
   -e OPENGPT_LOG_LEVEL=info \
   gngpp/opengpt:latest serve run
