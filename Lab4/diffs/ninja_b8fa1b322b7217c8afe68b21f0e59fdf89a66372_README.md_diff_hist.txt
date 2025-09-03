diff --git a/README.md b/README.md
index 9adc32d..52eeea6 100644
--- a/README.md
+++ b/README.md
@@ -31,12 +31,12 @@ Reverse engineered `ChatGPT` proxy (bypass Cloudflare 403 Access Denied)
 
 ### ArkoseLabs
 
-Sending `GPT4/GPT-3.5 (already grayscale)/Creating API-Key` dialog requires sending `Arkose Token` as a parameter. There are only two supported solutions for the time being.
+Sending `GPT4/GPT-3.5/Creating API-Key` dialog requires sending `Arkose Token` as a parameter. There are only two supported solutions for the time being.
 
 1) Use HAR
 
    - Supports HAR feature pooling, multiple HARs can be uploaded at the same time, and the usage strategy is random request.
-   > The `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads the `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` interface. HAR log file, use the startup parameter `--arkose-gpt4-har-dir` to specify the HAR directory path to use (if you do not specify a path, use the default path `~/.chat4.openai.com.har`, you can directly upload and update HAR ), the same method applies to `GPT3.5` and other types. Supports WebUI to upload and update HAR, request path: `/har/upload`, optional upload authentication parameter: `--arkose-har-upload-key`. and
+   > The `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads the `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` interface. HAR log file, use the startup parameter `--arkose-gpt4-har-dir` to specify the HAR directory path to use (if you do not specify a path, use the default path `~/.gpt4`, you can directly upload and update HAR ), the same method applies to `GPT3.5` and other types. Supports WebUI to upload and update HAR, request path: `/har/upload`, optional upload authentication parameter: `--arkose-har-upload-key`
 
 2) Use [YesCaptcha](https://yescaptcha.com/i/1Cc5i4) / [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d)
     > The platform performs verification code parsing, start the parameter `--arkose-solver` to select the platform (use `YesCaptcha` by default), `--arkose-solver-key` fill in `Client Key`
@@ -51,16 +51,16 @@ Sending `GPT4/GPT-3.5 (already grayscale)/Creating API-Key` dialog requires send
 #### Public interface, `*` represents any `URL` suffix
 
 - ChatGPT-API
-  - <https://host:port/public-api/*>
-  - <https://host:port/backend-api/*>
+  - `/public-api/*`
+  - `/backend-api/*`
   
 - OpenAI-API
-  - <https://host:port/v1/*>
+  - `/v1/*`
 
 - Platform-API
-  - <https://host:port/dashboard/*>
+  - `/dashboard/*`
 - ChatGPT-To-API
-  - <https://host:port/to/v1/chat/completions>
+  - `/to/v1/chat/completions`
   > About using `ChatGPT` to `API`, use `AceessToken` directly as `API Key`, interface path: `/to/v1/chat/completions`
 
 #### API documentation
