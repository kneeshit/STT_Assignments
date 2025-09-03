diff --git a/README_zh.md b/README_zh.md
index 9ef1d4a..8a57740 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -157,9 +157,9 @@ os=macos ./build_cross.sh # 默认在Macos上构建Macos平台
 # 编译单个平台二进制，以 aarch64-unknown-linux-musl 为例:
 docker run --rm -it \
   -v $(pwd):/home/rust/src \
-  -v $HOME/.cargo/registry:/root/.cargo/registry \  # 如果你希望使用本地缓存
-  -v $HOME/.cargo/git:/root/.cargo/git \  # 如果你希望使用本地缓存
-  ghcr.io/gngpp/opengpt-builder:aarch64-unknown-linux-musl \
+  -v $HOME/.cargo/registry:/root/.cargo/registry \
+  -v $HOME/.cargo/git:/root/.cargo/git \
+  ghcr.io/gngpp/opengpt-builder:x86_64-unknown-linux-musl \
   cargo build --release
 ```
 
