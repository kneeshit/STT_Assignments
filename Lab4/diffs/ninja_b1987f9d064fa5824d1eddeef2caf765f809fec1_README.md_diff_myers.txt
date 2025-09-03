diff --git a/README.md b/README.md
index b26ded3..8c0ac44 100644
--- a/README.md
+++ b/README.md
@@ -33,12 +33,11 @@ Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter,
 
 1) The endpoint obtained by `Arkose Token`, no matter what method you use, use `--arkose-token-endpoint` to specify the endpoint to obtain the token. The supported `JSON` format is generally in accordance with the format of the community: `{"token": "xxxxxx"}`
 
-2) The `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` interface The HAR logging file, and then use the startup parameter `--arkose-har-path` to specify the HAR file path using
+2) The `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` interface The HAR log record file, use the startup parameter `--arkose-har-path` to specify the HAR file path to use. Support uploading and updating HAR `request path: /har/upload`, the HAR file must exist, at this time, uploading and updating the HAR file is supported, optional upload authentication parameter `--arkose-har-upload-key`
 
-3) Use the [YesCaptcha](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/overview?homepageId=33020) platform for AI coding, the price is affordable, `10RMB` is calculated by point submission, `10000/ 3 ~= 3333 commits`
+3) Use the [YesCaptcha](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/overview?homepageId=33020) platform for AI coding, start the parameter `--arkose-yescaptcha-key` fill in the Key to enable, Affordable price, `10RMB` is calculated by point submission, `10000/3 ~= 3333 submissions`,
 
-All three schemes are used, and the priority is: `HAR` > `Arkose Token endpoint` > `YesCaptcha`.
-Support uploading and updating HAR `Request Path: /har/upload`, the HAR file path must be added at startup, and the file exists, then uploading and updating HAR files is supported.
+All three schemes are used, and the priority is: `HAR` > `Arkose Token endpoint` > `YesCaptcha`
 
 ### Platform Support
 
@@ -212,8 +211,10 @@ Options:
           Get arkose token endpoint
   -a, --arkose-har-path <ARKOSE_HAR_PATH>
           About the browser HAR file path requested by ArkoseLabs
+  -K, --arkose-har-upload-key <ARKOSE_HAR_UPLOAD_KEY>
+          HAR file upload authenticate key
   -Y, --arkose-yescaptcha-key <ARKOSE_YESCAPTCHA_KEY>
-          About the yescaptcha platform client key solved by ArkoseLabs
+          About the YesCaptcha platform client key solved by ArkoseLabs
   -S, --sign-secret-key <SIGN_SECRET_KEY>
           Enable url signature (signature secret key)
   -T, --tb-enable
