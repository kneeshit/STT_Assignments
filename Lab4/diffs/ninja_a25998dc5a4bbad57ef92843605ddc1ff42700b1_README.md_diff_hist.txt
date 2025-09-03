diff --git a/README.md b/README.md
index 6677a9e..b0b7cb0 100644
--- a/README.md
+++ b/README.md
@@ -33,7 +33,7 @@ Reverse engineered `ChatGPT` proxy (bypass Cloudflare 403 Access Denied)
 Sending `GPT4/GPT-3.5 (already grayscale)/Creating API-Key` dialog requires sending `Arkose Token` as a parameter. There are only two supported solutions for the time being.
 
 1) Use HAR
-    > The `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads the `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` interface. HAR log file, use the startup parameter `--arkose-chat4-har-file` to specify the HAR file path to use (if you do not specify a path, use the default path `~/.chat4.openai.com.har`, you can directly upload and update HAR ), supports uploading and updating HAR, request path: `/har/upload`, optional upload authentication parameter: `--arkose-har-upload-key`
+    > The `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads the `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` interface. HAR log file, use the startup parameter `--arkose-gpt4-har-dir` to specify the HAR file path to use (if you do not specify a path, use the default path `~/.chat4.openai.com.har`, you can directly upload and update HAR ), supports uploading and updating HAR, request path: `/har/upload`, optional upload authentication parameter: `--arkose-har-upload-key`
 
 2) Use [YesCaptcha](https://yescaptcha.com/i/1Cc5i4) / [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d)
     > The platform performs verification code parsing, start the parameter `--arkose-solver` to select the platform (use `YesCaptcha` by default), `--arkose-solver-key` fill in `Client Key`
@@ -41,7 +41,7 @@ Sending `GPT4/GPT-3.5 (already grayscale)/Creating API-Key` dialog requires send
 - Both solutions are used, the priority is: `HAR` > `YesCaptcha` / `CapSolver`
 - `YesCaptcha` / `CapSolver` is recommended to be used with HAR. When the verification code is generated, the parser is called for processing. After verification, HAR is more durable.
 
-> Currently OpenAI has updated `Login` which requires verification of `Arkose Token`. The solution is the same as GPT4. Fill in the startup parameters and specify the HAR file `--arkose-auth-har-file`. If you don't want to upload, you can log in through the browser code, which is not required. To create an API-Key, you need to upload the HAR feature file related to the Platform. The acquisition method is the same as above.
+> Currently OpenAI has updated `Login` which requires verification of `Arkose Token`. The solution is the same as GPT4. Fill in the startup parameters and specify the HAR file `--arkose-auth-har-dir`. If you don't want to upload, you can log in through the browser code, which is not required. To create an API-Key, you need to upload the HAR feature file related to the Platform. The acquisition method is the same as above.
 
 ### Http Server
 
@@ -230,14 +230,14 @@ Options:
           Cloudflare turnstile captcha secret key [env: CF_SITE_KEY=]
       --arkose-endpoint <ARKOSE_ENDPOINT>
           Arkose endpoint, Example: https://client-api.arkoselabs.com
-      --arkose-chat3-har-file <ARKOSE_CHAT3_HAR_FILE>
-          About the browser HAR file path requested by ChatGPT GPT-3.5 ArkoseLabs
-      --arkose-chat4-har-file <ARKOSE_CHAT4_HAR_FILE>
-          About the browser HAR file path requested by ChatGPT GPT-4 ArkoseLabs
-      --arkose-auth-har-file <ARKOSE_AUTH_HAR_FILE>
-          About the browser HAR file path requested by Auth ArkoseLabs
-      --arkose-platform-har-file <ARKOSE_PLATFORM_HAR_FILE>
-          About the browser HAR file path requested by Platform ArkoseLabs
+      --arkose-gpt3-har-dir <ARKOSE_CHAT3_HAR_FILE>
+          About the browser HAR directory path requested by ChatGPT GPT-3.5 ArkoseLabs
+      --arkose-gpt4-har-dir <ARKOSE_CHAT4_HAR_FILE>
+          About the browser HAR directory path requested by ChatGPT GPT-4 ArkoseLabs
+      --arkose-auth-har-dir <ARKOSE_AUTH_HAR_FILE>
+           About the browser HAR directory path requested by Auth ArkoseLabs
+      --arkose-platform-har-dir <ARKOSE_PLATFORM_HAR_FILE>
+          About the browser HAR directory path requested by Platform ArkoseLabs
   -K, --arkose-har-upload-key <ARKOSE_HAR_UPLOAD_KEY>
           HAR file upload authenticate key
   -s, --arkose-solver <ARKOSE_SOLVER>
