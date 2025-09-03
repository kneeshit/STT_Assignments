diff --git a/README_en.md b/README_en.md
index 19f5f3e..f92b004 100644
--- a/README_en.md
+++ b/README_en.md
@@ -123,6 +123,15 @@ Options:
 
 ### Compile
 
+- Linux musl current supports
+  - `x86_64-unknown-linux-musl`
+  - `aarch64-unknown-linux-musl`
+  - `armv7-unknown-linux-musleabi`
+  - `armv7-unknown-linux-musleabihf`
+  - `arm-unknown-linux-musleabi`
+  - `arm-unknown-linux-musleabihf`
+  - `armv5te-unknown-linux-musleabi`
+
 - Linux compile, Ubuntu machine for example:
 
 ```shell
@@ -135,6 +144,14 @@ git clone https://github.com/gngpp/opengpt.git && cd opengpt
 
 # Cross-platform compilation, relying on docker (if you can solve cross-platform compilation dependencies on your own)
 ./corss-build.sh
+
+# Compile a single platform binary, take aarch64-unknown-linux-musl as an example: 
+docker run --rm -it \
+  -v $(pwd):/home/rust/src \
+  -v $HOME/.cargo/registry:/root/.cargo/registry \  # If you want to use local cache
+  -v $HOME/.cargo/git:/root/.cargo/git \  # If you want to use local cache
+  ghcr.io/gngpp/opengpt-builder:aarch64-unknown-linux-musl \
+  cargo build --release
 ```
 
 - OpenWrt compile
