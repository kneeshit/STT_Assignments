diff --git a/README_zh.md b/README_zh.md
index 57ec23f..03a9c1e 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -10,6 +10,7 @@
   </a><a href="https://github.com/gngpp/opengpt/releases">
     <img src="https://img.shields.io/github/downloads/gngpp/opengpt/total?style=flat">
   </a>
+  [![](https://img.shields.io/docker/image-size/gngpp/opengpt)](https://registry.hub.docker.com/r/gngpp/opengpt)
   [![Docker Image](https://img.shields.io/docker/pulls/gngpp/opengpt.svg)](https://hub.docker.com/r/gngpp/opengpt/)
 
 # opengpt
@@ -54,12 +55,12 @@ GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest) 中有预编
 
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
@@ -144,7 +145,8 @@ git clone https://github.com/gngpp/opengpt.git && cd opengpt
 ./build.sh
 
 # 跨平台编译，依赖于docker(如果您可以自己解决跨平台编译依赖)，编译所有支持平台
-./corss-build.sh
+./build_cross.sh # 默认使用docker构建linux/windows平台
+os=macos ./build_cross.sh # 默认在Macos上构建Macos平台
 
 # 编译单个平台二进制，以 aarch64-unknown-linux-musl 为例:
 docker run --rm -it \
