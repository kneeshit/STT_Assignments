diff --git a/README.md b/README.md
index 16b607e..229a6fd 100644
--- a/README.md
+++ b/README.md
@@ -28,13 +28,6 @@ Reverse engineered `ChatGPT` proxy (bypass Cloudflare 403 Access Denied)
 
 > Limitations: This cannot bypass OpenAI's outright IP ban
 
-### Bypass IP restrictions
-
-Here `IP limit` refers to `OpenAI`'s request rate limit for `single IP`. You need to understand what `puid` is. The default request models interface returns `puid cookie`.
-In addition, the `GPT-4` session must be sent with `puid`. When using a third-party client to send a `GPT-4` conversation, the `puid` may not be saved or obtained. You need to handle it on the server side:
-
-- Use the startup parameter `--puid-user` to set the `Account Plus` account to obtain the `puid`, and it will be updated regularly
-
 ### ArkoseLabs
 
 Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter, and there are only three supported solutions for the time being
@@ -233,8 +226,6 @@ Options:
           TLS certificate file path [env: TLS_CERT=]
       --tls-key <TLS_KEY>
           TLS private key file path (EC/PKCS8/RSA) [env: TLS_KEY=]
-      --puid-user <PUID_USER>
-          Obtain the PUID of the Plus account user, Example: `user:pass`
       --api-prefix <API_PREFIX>
           WebUI api prefix [env: API_PREFIX=]
       --preauth-api <PREAUTH_API>
