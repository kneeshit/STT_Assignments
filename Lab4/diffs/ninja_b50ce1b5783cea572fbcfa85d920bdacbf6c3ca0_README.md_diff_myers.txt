diff --git a/README.md b/README.md
index e86ce78..6677a9e 100644
--- a/README.md
+++ b/README.md
@@ -172,6 +172,7 @@ Commands:
   restart  Restart the HTTP server daemon
   status   Status of the Http server daemon process
   log      Show the Http server daemon log
+  genca    Generate MITM CA certificate
   gt       Generate config template file (toml format file)
   help     Print this message or the help of the given subcommand(s)
 
@@ -200,7 +201,7 @@ Options:
   -i, --interface <INTERFACE>
           Bind address for outgoing connections (or IPv6 subnet fallback to Ipv4) [env: INTERFACE=]
   -I, --ipv6-subnet <IPV6_SUBNET>
-          IPv6 subnet, Example: 2001:19f0:6001:48e4::/64 [env: IPV4_SUBNET=]
+          IPv6 subnet, Example: 2001:19f0:6001:48e4::/64 [env: IPV6_SUBNET=]
       --disable-direct
           Disable direct connection [env: DISABLE_DIRECT=]
       --cookie-store
@@ -221,8 +222,6 @@ Options:
           Login Authentication Key [env: AUTH_KEY=]
       --api-prefix <API_PREFIX>
           WebUI api prefix [env: API_PREFIX=]
-      --preauth-api <PREAUTH_API>
-          PreAuth Cookie API URL [env: PREAUTH_API=] [default: https://ai.fakeopen.com/auth/preauth]
   -D, --disable-webui
           Disable WebUI [env: DISABLE_WEBUI=]
       --cf-site-key <CF_SITE_KEY>
@@ -257,13 +256,13 @@ Options:
           Token bucket fill rate [default: 1]
       --tb-expired <TB_EXPIRED>
           Token bucket expired (seconds) [default: 86400]
-  -B, --preauth-bind <PREAUTH_BIND>
-          Preauth MITM server bind address [env: PREAUTH_BIND=] [default: 0.0.0.0:8000]
-  -X, --preauth-upstream <PREAUTH_UPSTREAM>
-          Preauth MITM server upstream proxy [env: PREAUTH_UPSTREAM=]
-      --preauth-cert <PREAUTH_CERT>
+  -B, --pbind <PBIND>
+          Preauth MITM server bind address [env: PREAUTH_BIND=]
+  -X, --pupstream <PUPSTREAM>
+          Preauth MITM server upstream proxy, Only support http protocol [env: PREAUTH_UPSTREAM=]
+      --pcert <PCERT>
           Preauth MITM server CA certificate file path [default: ca/cert.crt]
-      --preauth-key <PREAUTH_KEY>
+      --pkey <PKEY>
           Preauth MITM server CA private key file path [default: ca/key.pem]
   -h, --help
           Print help
