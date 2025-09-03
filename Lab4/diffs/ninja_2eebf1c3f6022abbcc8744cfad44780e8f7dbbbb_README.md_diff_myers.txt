diff --git a/README.md b/README.md
index de85c29..bcb7cba 100644
--- a/README.md
+++ b/README.md
@@ -20,59 +20,60 @@ Reverse engineered `ChatGPT` proxy (bypass Cloudflare 403 Access Denied)
 ### Features
 
 - API key acquisition
-- Email/password account authentication (Google/Microsoft third-party login is temporarily not supported)
-- `Unofficial`/`Official`/`ChatGPT-to-API` Http API proxy (for third-party client access)
-- Support IP proxy pool
-- Minimal memory usage
+- Email/password account authentication (Google/Microsoft third-party login not supported)
+- `ChatGPT-API`/`OpenAI-API`/`ChatGPT-to-API` Http API proxy (for third-party client access)
+- Support IP proxy pool (support using Ipv6 subnet as proxy pool)
 - ChatGPT WebUI
+- Very small memory footprint
 
 > Limitations: This cannot bypass OpenAI's outright IP ban
 
 ### ArkoseLabs
 
-Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter, and there are only three supported solutions for the time being
+Sending `GPT4/GPT-3.5 (already grayscale)` dialogue requires sending `Arkose Token` as a parameter. There are currently only three supported solutions.
 
-1) The endpoint obtained by `Arkose Token`, no matter what method you use, use `--arkose-token-endpoint` to specify the endpoint to obtain the token. The supported `JSON` format is generally in accordance with the format of the community: `{"token": "xxxxxx"}`
+1) Using HAR, `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` For the HAR log file of the interface, use the startup parameter `--arkose-chat4-har-file` to specify the HAR file path to use (if the path is not specified, the default path `~/.chat4.openai.com.har` will be used, and updates can be uploaded directly HAR), supports uploading and updating HAR, request path: `/har/upload`, optional upload authentication parameter: `--arkose-har-upload-key`
 
-2) Using HAR, `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` For the HAR log file of the interface, use the startup parameter `--arkose-chat-har-file` to specify the HAR file path to use (if the path is not specified, the default path `~/.chat.openai.com.har` will be used, and updates can be uploaded directly HAR), supports uploading and updating HAR, request path: `/har/upload`, optional upload authentication parameter: `--arkose-har-upload-key`
-
-3) Use [YesCaptcha](https://yescaptcha.com/i/1Cc5i4)/[CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d) platform for verification code parsing, start the parameter `--arkose-solver` to select the platform (the default is `YesCaptcha`), `--arkose-solver-key` fill in `Client Key`
+2) Use [YesCaptcha](https://yescaptcha.com/i/1Cc5i4)/[CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d) platform for verification code parsing, start the parameter `--arkose-solver` to select the platform (the default is `YesCaptcha`), `--arkose-solver-key` fill in `Client Key`
 
 - All three solutions are used, the priority is: `HAR` > `YesCaptcha/CapSolver` > `Arkose Token endpoint`
 - `YesCaptcha/CapSolver` is recommended to be used with HAR. When the verification code is generated, the parser is called for processing. After verification, HAR is more durable.
 
 > Currently OpenAI has updated that login requires verification of `Arkose Token`. The solution is the same as GPT4. Fill in the startup parameters and specify the HAR file `--arkose-auth-har-file`. If you don't want to upload, you can log in through the browser code, which is not required.
 
-### Command Line(dev)
-
 ### Http Server
 
 #### Public interface, `*` represents any `URL` suffix
 
-- backend-api, <https://host:port/backend-api/*>
-- public-api, <https://host:port/public-api/*>
-- platform-api, <https://host:port/v1/*>
-- dashboard-api, <https://host:port/dashboard/*>
-- chatgpt-to-api, <https://host:port/to/v1/chat/completions>
+- ChatGPT-API
+  - <https://host:port/public-api/*>
+  - <https://host:port/backend-api/*>
+  
+- OpenAI-API
+  - <https://host:port/v1/*>
+
+- Platform-API
+  - <https://host:port/dashboard/*>
+- ChatGPT-To-API
+  - <https://host:port/to/v1/chat/completions>
+  > About using `ChatGPT` to `API`, use `AceessToken` directly as `API Key`, interface path: `/to/v1/chat/completions`
 
 #### API documentation
 
 - Platfrom API [doc](https://platform.openai.com/docs/api-reference)
 - Backend API [doc](doc/rest.http)
 
-> About using `ChatGPT` to `API`, use `AceessToken` directly as `API Key`, interface path: `/to/v1/chat/completions`
-
 #### Basic services
 
-- Authentic ChatGPT WebUI
-- Expose `unofficial`/`official API` proxies
-- The `API` prefix is consistent with the official
-- `ChatGPT` To `API`
-- Accessible to third-party clients
-- Access to IP proxy pool to improve concurrency
-- API documentation
+- ChatGPT WebUI
+- Expose `ChatGPT-API`/`OpenAI-API` proxies
+- `API` prefix is consistent with the official one
+- `ChatGPT` to `API`
+- Can access third-party clients
+- Can access IP proxy pool to improve concurrency
+
+#### Parameter Description
 
-- Parameter Description
 - `--level`, environment variable `LOG`, log level: default info
 - `--bind`, environment variable `BIND`, service listening address: default 0.0.0.0:7999,
 - `--tls-cert`, environment variable `TLS_CERT`', TLS certificate public key. Supported format: EC/PKCS8/RSA
@@ -101,12 +102,12 @@ There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/n
 
 ```shell
 wget https://github.com/gngpp/ninja/releases/download/v0.7.2/ninja_0.7.2_aarch64_generic.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.7.2/luci-app-ninja_1.1.3-1_all.ipk
-wget https://github.com/gngpp/ninja/releases/download/v0.7.2/luci-i18n-ninja-zh-cn_1.1.3-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.7.2/luci-app-ninja_1.1.4-1_all.ipk
+wget https://github.com/gngpp/ninja/releases/download/v0.7.2/luci-i18n-ninja-zh-cn_1.1.4-1_all.ipk
 
 opkg install ninja_0.7.2_aarch64_generic.ipk
-opkg install luci-app-ninja_1.1.3-1_all.ipk
-opkg install luci-i18n-ninja-zh-cn_1.1.3-1_all.ipk
+opkg install luci-app-ninja_1.1.4-1_all.ipk
+opkg install luci-i18n-ninja-zh-cn_1.1.4-1_all.ipk
 ```
 
 - #### Docker
