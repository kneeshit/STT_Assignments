diff --git a/README.md b/README.md
index e8c32ab..9c17a32 100644
--- a/README.md
+++ b/README.md
@@ -73,6 +73,8 @@ Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter,
 >
 > - Platform API [doc](https://platform.openai.com/docs/api-reference)
 > - Backend API [doc](doc/rest.http)
+>
+> About using `ChatGPT` to `API`, use `AceessToken` directly as `API Key`, the interface path `https://host:port/to/v1/chat/completions`
 
 - Authentic ChatGPT WebUI
 - Expose `unofficial`/`official API` proxies
@@ -88,10 +90,10 @@ Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter,
   - `--port`, environment variable `PORT`, listening port: default 7999
   - `--tls-cert`, environment variable `TLS_CERT`', TLS certificate public key. Supported format: EC/PKCS8/RSA
   - `--tls-key`, environment variable `TLS_KEY`, TLS certificate private key
-  - `--proxies`, Proxy, supports proxy pool, multiple proxies are separated by `,`, format: protocol://user:pass@ip:port, if the IP is Banned, it is recommended to turn off the use of direct IP when using the proxy pool, `--disable-direct`turn off direct connection
+  - `--proxies`, Proxy, supports proxy pool, multiple proxies are separated by `,`, format: protocol://user:pass@ip:port, if the local IP is banned, you need to turn off the use of direct IP when using the proxy pool, `-- disable-direct` turns off direct connection, otherwise your banned local IP will be used according to load balancing
   - `--workers`, worker threads: default 1
 
-...
+[...](https://github.com/gngpp/ninja/blob/main/README.md#command-manual)
 
 ### Install
 
