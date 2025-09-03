diff --git a/README.md b/README.md
index 6aff3eb..605acd4 100644
--- a/README.md
+++ b/README.md
@@ -49,6 +49,8 @@ Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter,
 - All three solutions are used, the priority is: `HAR` > `YesCaptcha/CapSolver` > `Arkose Token endpoint`
 - `YesCaptcha/CapSolver` is recommended to be used with HAR. When the verification code is generated, the parser is called for processing. After verification, HAR is more durable.
 
+> Currently OpenAI has updated that login requires verification of `Arkose Token`. The solution is the same as GPT4. Fill in the startup parameters and specify the HAR file `--arkose-auth-har-file`
+
 ### Command Line(dev)
 
 ### Http Server
@@ -214,12 +216,12 @@ Options:
           Arkose endpoint, Example: https://client-api.arkoselabs.com
   -A, --arkose-token-endpoint <ARKOSE_TOKEN_ENDPOINT>
           Get arkose token endpoint
-      --arkose-chat-har-path <ARKOSE_CHAT_HAR_PATH>
+      --arkose-chat-har-file <ARKOSE_CHAT_HAR_FILE>
           About the browser HAR file path requested by ChatGPT ArkoseLabs
-      --arkose-platform-har-path <ARKOSE_PLATFORM_HAR_PATH>
-          About the browser HAR file path requested by Platform ArkoseLabs
-      --arkose-auth-har-path <ARKOSE_AUTH_HAR_PATH>
+      --arkose-auth-har-file <ARKOSE_AUTH_HAR_FILE>
           About the browser HAR file path requested by Auth ArkoseLabs
+      --arkose-platform-har-file <ARKOSE_PLATFORM_HAR_FILE>
+          About the browser HAR file path requested by Platform ArkoseLabs
   -K, --arkose-har-upload-key <ARKOSE_HAR_UPLOAD_KEY>
           HAR file upload authenticate key
   -s, --arkose-solver <ARKOSE_SOLVER>
