diff --git a/README.md b/README.md
index 52f86cf..93e479a 100644
--- a/README.md
+++ b/README.md
@@ -56,9 +56,45 @@ All three schemes are used, and the priority is: `HAR` > `Arkose Token endpoint`
   - `x86_64-apple-darwin`
   - `aarch64-apple-darwin`
 
+### Command Line(dev)
+
+### Http Server
+
+> Public API, `*` means any `URL` suffix
+>
+> - backend-api, <https://host:port/backend-api/*>
+> - public-api, <https://host:port/public-api/*>
+> - platform-api, <https://host:port/v1/*>
+> - dashboard-api, <https://host:port/dashboard/*>
+> - chatgpt-to-api, <https://host:port/to/v1/chat/completions>
+>
+> Detailed API documentation
+>
+> - Platform API [doc](https://platform.openai.com/docs/api-reference)
+> - Backend API [doc](doc/rest.http)
+
+- Authentic ChatGPT WebUI
+- Expose `unofficial`/`official API` proxies
+- The `API` prefix is consistent with the official
+- `ChatGPT` To `API`
+- Accessible to third-party clients
+- Access to IP proxy pool to improve concurrency
+- API documentation
+
+- Parameter Description
+  - `--level`, environment variable `LOG`, log level: default info
+  - `--host`, environment variable `HOST`, service listening address: default 0.0.0.0,
+  - `--port`, environment variable `PORT`, listening port: default 7999
+  - `--tls-cert`, environment variable `TLS_CERT`', TLS certificate public key. Supported format: EC/PKCS8/RSA
+  - `--tls-key`, environment variable `TLS_KEY`, TLS certificate private key
+  - `--proxies`, Proxy, supports proxy pool, multiple proxies are separated by `,`, format: protocol://user:pass@ip:port, if the IP is Banned, it is recommended to turn off the use of direct IP when using the proxy pool, `--disable -direct`turn off direct connection
+  - `--workers`, worker threads: default 1
+
+...
+
 ### Install
 
-  > #### Ubuntu(Other Linux)
+- #### Ubuntu(Other Linux)
 
 Making [Releases](https://github.com/gngpp/opengpt/releases/latest) has a precompiled deb package, binaries, in Ubuntu, for example:
 
@@ -68,7 +104,7 @@ dpkg -i opengpt-0.4.9-x86_64-unknown-linux-musl.deb
 opengpt serve run
 ```
 
-> #### OpenWrt
+- #### OpenWrt
 
 There are pre-compiled ipk files in GitHub [Releases](https://github.com/gngpp/opengpt/releases/latest), which currently provide versions of aarch64/x86_64 and other architectures. After downloading, use opkg to install, and use nanopi r4s as example:
 
@@ -82,7 +118,7 @@ opkg install luci-app-opengpt_1.0.6-1_all.ipk
 opkg install luci-i18n-opengpt-zh-cn_1.0.6-1_all.ipk
 ```
 
-> #### Docker
+- #### Docker
 
 ```shell
 docker run --rm -it -p 7999:7999 --name=opengpt \
@@ -91,7 +127,7 @@ docker run --rm -it -p 7999:7999 --name=opengpt \
   gngpp/opengpt:latest serve run
 ```
 
-> docker-compose
+- Docker Compose
 
 ```yaml
 version: '3'
@@ -133,41 +169,7 @@ services:
 
 ```
 
-### Command Line(dev)
-
-### Http Server
-
-> Public API, `*` means any `URL` suffix
->
-> - backend-api, <https://host:port/backend-api/*>
-> - public-api, <https://host:port/public-api/*>
-> - platform-api, <https://host:port/v1/*>
-> - dashboard-api, <https://host:port/dashboard/*>
-> - chatgpt-to-api, <https://host:port/to/v1/chat/completions>
->
-> Detailed API documentation
->
-> - Platform API [doc](https://platform.openai.com/docs/api-reference)
-> - Backend API [doc](doc/rest.http)
-
-- Authentic ChatGPT WebUI
-- Expose `unofficial`/`official API` proxies
-- The `API` prefix is consistent with the official
-- `ChatGPT` To `API`
-- Accessible to third-party clients
-- Access to IP proxy pool to improve concurrency
-- API documentation
-
-- Parameter Description
-  - `--level`, environment variable `LOG`, log level: default info
-  - `--host`, environment variable `HOST`, service listening address: default 0.0.0.0,
-  - `--port`, environment variable `PORT`, listening port: default 7999
-  - `--tls-cert`, environment variable `TLS_CERT`', TLS certificate public key. Supported format: EC/PKCS8/RSA
-  - `--tls-key`, environment variable `TLS_KEY`, TLS certificate private key
-  - `--proxies`, proxies，support multiple proxy pools, format: protocol://user:pass@ip:port
-  - `--workers`, worker threads: default 1
-
-...
+### Command Manual
 
 ```shell
 $ opengpt serve --help
@@ -188,8 +190,10 @@ Options:
           Server worker-pool size (Recommended number of CPU cores) [default: 1]
       --concurrent-limit <CONCURRENT_LIMIT>
           Enforces a limit on the concurrent number of requests the underlying [default: 65535]
-      --proxies <PROXIES>
+  -x, --proxies <PROXIES>
           Server proxies pool, Example: protocol://user:pass@ip:port [env: PROXIES=]
+      --disable-direct
+          Disable direct connection [env: DISABLE_DIRECT=]
       --timeout <TIMEOUT>
           Client timeout (seconds) [default: 600]
       --connect-timeout <CONNECT_TIMEOUT>
