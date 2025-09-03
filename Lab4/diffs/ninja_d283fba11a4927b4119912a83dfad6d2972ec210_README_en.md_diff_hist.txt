diff --git a/README_en.md b/README_en.md
index ce584f2..be5ca07 100644
--- a/README_en.md
+++ b/README_en.md
@@ -1,3 +1,5 @@
+<br>English | [简体中文](README.md)
+
 [![CI](https://github.com/gngpp/opengpt/actions/workflows/CI.yml/badge.svg)](https://github.com/gngpp/opengpt/actions/workflows/CI.yml)
 <a href="/LICENSE">
     <img src="https://img.shields.io/github/license/gngpp/opengpt?style=flat">
@@ -9,8 +11,6 @@
   </a>
   [![Docker Image](https://img.shields.io/docker/pulls/gngpp/opengpt.svg)](https://hub.docker.com/r/gngpp/opengpt/)
 
-<br>English | [简体中文](README.md)
-
 # opengpt
 
 Not just an unofficial ChatGPT proxy (bypass Cloudflare 403 Access Denied)
@@ -21,23 +21,9 @@ Not just an unofficial ChatGPT proxy (bypass Cloudflare 403 Access Denied)
 
 > Limitations: This cannot bypass OpenAI's outright IP ban
 
-### Compile
+### Install
 
-> Ubuntu machine for example:
-
-```shell
-
-sudo apt update -y && sudo apt install rename
-
-# Native compilation
-git clone https://github.com/gngpp/opengpt.git && cd opengpt
-./build.sh
-
-# Cross-platform compilation, relying on docker (if you can solve cross-platform compilation dependencies on your own)
-./corss-build.sh
-```
-
-### Ubuntu(Other Linux)
+  > #### Ubuntu(Other Linux)
 
 Making [Releases](https://github.com/gngpp/opengpt/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
@@ -49,16 +35,18 @@ dpkg -i opengpt-0.1.1-x86_64-unknown-linux-musl.deb
 opengpt serve
 ```
 
-### Docker
+> #### Docker
 
 ```shell
 docker run --rm -it -p 7999:7999 --hostname=opengpt \
+  -e OPENGPT_WORKERS=1 \
+  -e OPENGPT_LOG_LEVEL=info \
   -e OPENGPT_TLS_CERT=/path/to/cert \
   -e OPENGPT_TLS_KEY=/path/to/key \
-  gngpp/opengpt:latest opengpt serve
+  gngpp/opengpt:latest serve
 ```
 
-### OpenWrt(dev)
+> #### OpenWrt(dev)
 
 ### Command Line(dev)
 
@@ -120,6 +108,22 @@ Options:
           Print help
 ```
 
+### Compile
+
+> Ubuntu machine for example:
+
+```shell
+
+sudo apt update -y && sudo apt install rename
+
+# Native compilation
+git clone https://github.com/gngpp/opengpt.git && cd opengpt
+./build.sh
+
+# Cross-platform compilation, relying on docker (if you can solve cross-platform compilation dependencies on your own)
+./corss-build.sh
+```
+
 ### Reference
 
 - <https://github.com/tjardoo/openai-client>
