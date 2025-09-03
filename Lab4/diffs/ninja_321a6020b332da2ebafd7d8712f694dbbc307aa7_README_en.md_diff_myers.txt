diff --git a/README_en.md b/README_en.md
index 3f74a25..1b8a849 100644
--- a/README_en.md
+++ b/README_en.md
@@ -28,6 +28,14 @@ Reverse engineered `ChatGPT` proxy (bypass Cloudflare 403 Access Denied)
 
 > Limitations: This cannot bypass OpenAI's outright IP ban
 
+### Bypass IP restrictions
+
+Here `IP limit` refers to `OpenAI`'s request rate limit for `single IP`. You need to understand what `puid` is. The default request models interface returns `puid cookie`.
+In addition, the `GPT-4` session must be sent with `puid`. When using a third-party client to send a `GPT-4` reply, the `puid` may not be saved or obtained. You need to handle it on the server side:
+
+- Use the startup parameter `--puid` to set up shared use separately. This method does not support updates.
+- Use the startup parameter `--puid-user` to set the `Account Plus` account to obtain the `puid`, and it will be updated regularly
+
 ### ArkoseLabs
 
 Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter, and there are only three supported solutions for the time being
@@ -36,7 +44,7 @@ Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter,
 
 2) Using HAR, `ChatGPT` official website sends a `GPT4` session message, and the browser `F12` downloads `https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97- 6ADB7EFF8147` For the HAR log file of the interface, use the startup parameter `--arkose-har-file` to specify the HAR file path to use (if the path is not specified, the default path `~/chat.openai.com.har` will be used, and updates can be uploaded directly HAR), supports uploading and updating HAR, request path: `/har/upload`, optional upload authentication parameter: `--arkose-har-upload-key`
 
-3) Use [YesCaptcha](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/overview?homepageId=33020)/[CapSolver](https://docs.capsolver.com/guide/why-choose-capsolver.html) platform for verification code parsing, start the parameter `--arkose-solver` to select the platform (the default is `YesCaptcha`), `--arkose-solver-key` fill in `Client Key`
+3) Use [YesCaptcha](https://yescaptcha.com/i/1Cc5i4)/[CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=y7CtB_a-3X6d) platform for verification code parsing, start the parameter `--arkose-solver` to select the platform (the default is `YesCaptcha`), `--arkose-solver-key` fill in `Client Key`
 
 - All three solutions are used, the priority is: `HAR` > `YesCaptcha/CapSolver` > `Arkose Token endpoint`
 - `YesCaptcha/CapSolver` is recommended to be used with HAR. When the verification code is generated, the parser is called for processing. After verification, HAR is more durable.
