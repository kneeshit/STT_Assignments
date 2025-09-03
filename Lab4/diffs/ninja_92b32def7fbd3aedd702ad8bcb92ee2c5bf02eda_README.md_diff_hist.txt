diff --git a/README.md b/README.md
index 65bd61c..b93a402 100644
--- a/README.md
+++ b/README.md
@@ -22,6 +22,7 @@ A reverse engineered unofficial `ChatGPT` proxy (bypass Cloudflare 403 Access De
 - API key acquisition
 - Email/password account authentication (Google/Microsoft third-party login is not supported for now because the author does not have an account)
 - Unofficial/Official Http API proxy (for third-party client access)
+- ChatGPT to API
 - The original ChatGPT WebUI
 - Minimal memory usage
 
@@ -138,11 +139,25 @@ opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
 
 ### Http Server
 
+> Public API, `*` means any `URL` suffix
+>
+> - backend-api, <https://host:port/backend-api/*>
+> - public-api, <https://host:port/public-api/*>
+> - platform-api, <https://host:port/v1/*>
+> - dashboard-api, <https://host:port/dashboard/*>
+> - chatgpt-to-api, <https://host:port/conv/v1/chat/completions>
+>
+> Detailed API documentation
+>
+> - Platform API [doc](https://platform.openai.com/docs/api-reference)
+> - Backend API [doc](doc/rest.http)
+
 - Authentic ChatGPT WebUI
-- Support unofficial/official API proxy
-- The API prefix is consistent with the official
+- Expose `unofficial`/`official API` proxies
+- The `API` prefix is consistent with the official
+- `ChatGPT` To `API`
 - Accessible to third-party clients
-- Access to IP proxy pool to increase concurrency
+- Access to IP proxy pool to improve concurrency
 - API documentation
 
 - Parameter Description
@@ -158,6 +173,8 @@ opkg install luci-i18n-opengpt-zh-cn_1.0.2-1_all.ipk
   - `--tls-key`, environment variable `OPENGPT_TLS_KEY`, TLS certificate private key
   - `--proxies`, environment variable `OPENGPT_PROXY`, proxies，support multiple proxy pools, format: protocol://user:pass@ip:port
 
+...
+
 ```shell
 $ opengpt serve --help
 Start the http server
@@ -216,8 +233,10 @@ git clone https://github.com/gngpp/opengpt.git && cd opengpt
 ./build.sh
 
 # Cross-platform compilation, relying on docker (if you can solve cross-platform compilation dependencies on your own)
-./build_cross.sh # Default using docker build linux/windows platform 
-os=macos ./build_cross.sh # The MacOS platform is built on MacOS by default
+# Default using docker build linux/windows platform 
+./build_cross.sh
+# The MacOS platform is built on MacOS by default
+os=macos ./build_cross.sh 
 
 # Compile a single platform binary, take aarch64-unknown-linux-musl as an example: 
 docker run --rm -it --user=$UID:$(id -g $USER) \
