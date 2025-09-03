diff --git a/README_zh.md b/README_zh.md
index f3c3ea3..036c787 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -2,8 +2,8 @@
 
 [![CI](https://github.com/gngpp/ninja/actions/workflows/CI.yml/badge.svg)](https://github.com/gngpp/ninja/actions/workflows/CI.yml)
 [![CI](https://github.com/gngpp/ninja/actions/workflows/Release.yml/badge.svg)](https://github.com/gngpp/ninja/actions/workflows/Release.yml)
- <a target="_blank" href="https://github.com/gngpp/vdns/blob/main/LICENSE">
-  <img src="https://img.shields.io/badge/license-MIT-blue.svg"/>
+ <a target="_blank" href="https://github.com/gngpp/ninja/blob/main/LICENSE">
+  <img src="https://img.shields.io/badge/license-GPL3.0-blue.svg"/>
  </a>
   <a href="https://github.com/gngpp/ninja/releases">
     <img src="https://img.shields.io/github/release/gngpp/ninja.svg?style=flat">
@@ -97,8 +97,8 @@
   GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 deb包，二进制文件，以Ubuntu为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.6.3/ninja-0.6.3-x86_64-unknown-linux-musl.deb
-dpkg -i ninja-0.6.3-x86_64-unknown-linux-musl.deb
+wget https://github.com/gngpp/ninja/releases/download/v0.6.4/ninja-0.6.4-x86_64-unknown-linux-musl.deb
+dpkg -i ninja-0.6.4-x86_64-unknown-linux-musl.deb
 ninja serve run
 ```
 
@@ -107,13 +107,13 @@ ninja serve run
 GitHub [Releases](https://github.com/gngpp/ninja/releases/latest) 中有预编译的 ipk 文件， 目前提供了 aarch64/x86_64 等架构的版本，下载后使用 opkg 安装，以 nanopi r4s 为例：
 
 ```shell
-wget https://github.com/gngpp/ninja/releases/download/v0.6.3/ninja_0.6.3_aarch64_generic.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.6.3/luci-app-ninja_1.0.9-1_all.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.6.3/luci-i18n-ninja-zh-cn_1.0.9-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.4/ninja_0.6.4_aarch64_generic.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.4/luci-app-ninja_1.1.2-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.6.4/luci-i18n-ninja-zh-cn_1.1.2-1_all.ipk
 
-opkg install ninja_0.6.3_aarch64_generic.ipk
-opkg install luci-app-ninja_1.0.9-1_all.ipk
-opkg install luci-i18n-ninja-zh-cn_1.0.9-1_all.ipk
+opkg install ninja_0.6.4_aarch64_generic.ipk
+opkg install luci-app-ninja_1.1.2-1_all.ipk
+opkg install luci-i18n-ninja-zh-cn_1.1.2-1_all.ipk
 ```
 
 - #### Docker
