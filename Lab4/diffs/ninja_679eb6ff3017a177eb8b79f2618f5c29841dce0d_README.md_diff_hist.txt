diff --git a/reqwest/README.md b/reqwest/README.md
index 2c7b60d..7b1f9a9 100644
--- a/reqwest/README.md
+++ b/reqwest/README.md
@@ -10,8 +10,8 @@ It is currently missing HTTP/2 `PRIORITY` support. (PRs to [h2](https://github.c
 
 ```toml
 [patch.crates-io]
-hyper = { git = "https://github.com/4JX/hyper.git", branch = "v0.14.18-patched" }
-h2 = { git = "https://github.com/4JX/h2.git", branch = "imp" }
+hyper = { git = "https://github.com/gngpp/hyper.git", branch = "v0.14.18-patched" }
+h2 = { git = "https://github.com/gngpp/h2.git", branch = "imp" }
 ```
 
 These patches were made specifically for `reqwest-impersonate` to work, but I would appreciate if someone took the time to PR more "proper" versions to the parent projects.
@@ -21,7 +21,7 @@ These patches were made specifically for `reqwest-impersonate` to work, but I wo
 `Cargo.toml`
 
 ```toml
-reqwest-impersonate = { git = "https://github.com/4JX/reqwest-impersonate.git", default-features = false, features = [
+reqwest-impersonate = { git = "https://github.com/gngpp/reqwest-impersonate.git", default-features = false, features = [
     "chrome",
     "blocking",
 ] }
