diff --git a/README.md b/README.md
index 54c4b0b..41978e3 100644
--- a/README.md
+++ b/README.md
@@ -34,7 +34,7 @@ Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter,
 
 1) The endpoint obtained by `Arkose Token`, no matter what method you use, use `--arkose-token-endpoint` to specify the endpoint to obtain the token. The supported `JSON` format is generally in accordance with the format of the community: `{"token": "xxxxxx"}`
 
-2) The `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147` interface The HAR log record file, use the startup parameter `--arkose-har-file` to specify the HAR file path to use. Support uploading and updating HAR `request path: /har/upload`, the HAR file must exist, at this time, uploading and updating the HAR file is supported, optional upload authentication parameter `--arkose-har-upload-key`
+2) Using HAR, `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97- 6ADB7EFF8147` Interface HAR log record file, use the startup parameter `--arkose-har-file` to specify the HAR file path (if the path is not specified, the default path is used, and HAR can be uploaded and updated directly). It supports uploading and updating HAR. Request path: `/har/upload`, optional upload authentication parameter: `--arkose-har-upload-key`
 
 3) Use [YesCaptcha](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/overview?homepageId=33020)/[CapSolver](https://docs.capsolver.com/guide/why-choose-capsolver.html) platform for verification code parsing, start the parameter `--arkose-solver` to select the platform (the default is `YesCaptcha`), `--arkose-solver-key` fill in `Client Key`
 
