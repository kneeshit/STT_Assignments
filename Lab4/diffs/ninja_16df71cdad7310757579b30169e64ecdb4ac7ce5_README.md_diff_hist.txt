diff --git a/README.md b/README.md
index c072639..9e494ef 100644
--- a/README.md
+++ b/README.md
@@ -10,6 +10,7 @@
   </a><a href="https://github.com/gngpp/opengpt/releases">
     <img src="https://img.shields.io/github/downloads/gngpp/opengpt/total?style=flat">
   </a>
+  [![](https://img.shields.io/docker/image-size/gngpp/opengpt)](https://registry.hub.docker.com/r/gngpp/opengpt)
   [![Docker Image](https://img.shields.io/docker/pulls/gngpp/opengpt.svg)](https://hub.docker.com/r/gngpp/opengpt/)
 
 # opengpt
@@ -54,12 +55,12 @@ There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/o
 
 ```shell
 wget https://github.com/gngpp/opengpt/releases/download/v0.1.7/opengpt_0.1.7_aarch64_generic.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.7/luci-app-opengpt_1.0.0-1_all.ipk
-wget https://github.com/gngpp/opengpt/releases/download/v0.1.7/luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.7/luci-app-opengpt_1.0.2-1_all.ipk
+wget https://github.com/gngpp/opengpt/releases/download/v0.1.7/luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
 opkg install opengpt_0.1.7_aarch64_generic.ipk
-opkg install luci-app-opengpt_1.0.0-1_all.ipk
-opkg install luci-i18n-opengpt-zh-cn_1.0.0-1_all.ipk
+opkg install luci-app-opengpt_1.0.2-1_all.ipk
+opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 ```
 
 ### Command Line(dev)
@@ -147,7 +148,8 @@ git clone https://github.com/gngpp/opengpt.git && cd opengpt
 ./build.sh
 
 # Cross-platform compilation, relying on docker (if you can solve cross-platform compilation dependencies on your own)
-./corss-build.sh
+./build_cross.sh # Default using docker build linux/windows platform 
+os=macos ./build_cross.sh # The MacOS platform is built on MacOS by default
 
 # Compile a single platform binary, take aarch64-unknown-linux-musl as an example: 
 docker run --rm -it \
