diff --git a/README_en.md b/README_en.md
index 03b689c..27ae77b 100644
--- a/README_en.md
+++ b/README_en.md
@@ -31,7 +31,7 @@ Reverse engineered `ChatGPT` proxy (bypass Cloudflare 403 Access Denied)
 ### Bypass IP restrictions
 
 Here `IP limit` refers to `OpenAI`'s request rate limit for `single IP`. You need to understand what `puid` is. The default request models interface returns `puid cookie`.
-In addition, the `GPT-4` session must be sent with `puid`. When using a third-party client to send a `GPT-4` reply, the `puid` may not be saved or obtained. You need to handle it on the server side:
+In addition, the `GPT-4` session must be sent with `puid`. When using a third-party client to send a `GPT-4` conversation, the `puid` may not be saved or obtained. You need to handle it on the server side:
 
 - Use the startup parameter `--puid` to set up shared use separately. This method does not support updates.
 - Use the startup parameter `--puid-user` to set the `Account Plus` account to obtain the `puid`, and it will be updated regularly
