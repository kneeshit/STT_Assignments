diff --git a/README.md b/README.md
index eec74ee..d8e3ba3 100644
--- a/README.md
+++ b/README.md
@@ -162,9 +162,9 @@ os=macos ./build_cross.sh # The MacOS platform is built on MacOS by default
 # Compile a single platform binary, take aarch64-unknown-linux-musl as an example: 
 docker run --rm -it \
   -v $(pwd):/home/rust/src \
-  -v $HOME/.cargo/registry:/root/.cargo/registry \  # If you want to use local cache
-  -v $HOME/.cargo/git:/root/.cargo/git \  # If you want to use local cache
-  ghcr.io/gngpp/opengpt-builder:aarch64-unknown-linux-musl \
+  -v $HOME/.cargo/registry:/root/.cargo/registry \
+  -v $HOME/.cargo/git:/root/.cargo/git \
+  ghcr.io/gngpp/opengpt-builder:x86_64-unknown-linux-musl \
   cargo build --release
 ```
 
