diff --git a/README.md b/README.md
index 34e35ba..41fcd2d 100644
--- a/README.md
+++ b/README.md
@@ -123,6 +123,15 @@ Options:
 
 ### 自行编译
   
+- Linux musl 目前支持
+  - `x86_64-unknown-linux-musl`
+  - `aarch64-unknown-linux-musl`
+  - `armv7-unknown-linux-musleabi`
+  - `armv7-unknown-linux-musleabihf`
+  - `arm-unknown-linux-musleabi`
+  - `arm-unknown-linux-musleabihf`
+  - `armv5te-unknown-linux-musleabi`
+
 - Linux编译，Ubuntu机器为例:
 
 ```shell
@@ -130,8 +139,16 @@ Options:
 git clone https://github.com/gngpp/opengpt.git && cd opengpt
 ./build.sh
 
-# 跨平台编译，依赖于docker(如果您可以自己解决跨平台编译依赖)
+# 跨平台编译，依赖于docker(如果您可以自己解决跨平台编译依赖)，编译所有支持平台
 ./corss-build.sh
+
+# 编译单个平台二进制，以 aarch64-unknown-linux-musl 为例:
+docker run --rm -it \
+  -v $(pwd):/home/rust/src \
+  -v $HOME/.cargo/registry:/root/.cargo/registry \  # 如果你希望使用本地缓存
+  -v $HOME/.cargo/git:/root/.cargo/git \  # 如果你希望使用本地缓存
+  ghcr.io/gngpp/opengpt-builder:aarch64-unknown-linux-musl \
+  cargo build --release
 ```
 
 - OpenWrt 编译
