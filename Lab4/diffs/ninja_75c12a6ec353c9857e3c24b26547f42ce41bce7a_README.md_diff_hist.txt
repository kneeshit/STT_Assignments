diff --git a/README.md b/README.md
index c6bbdd4..410cc43 100644
--- a/README.md
+++ b/README.md
@@ -95,6 +95,16 @@ Sending `GPT4/GPT-3.5 (already grayscale)/Creating API-Key` dialog requires send
 
 `About the method of obtaining Refresh Token`, use the `ChatGPT App` login method of the `Apple` platform. The principle is to use the built-in MITM agent. When the `Apple device` is connected to the agent, you can log in to the `Apple platform` to obtain `RefreshToken`. It is only suitable for small quantities or personal use `(large quantities will seal the device, use with caution)`. For detailed usage, please see the startup parameter description.
 
+```shell
+ # Generate certificate
+ ninja genca
+
+ ninja run --pbind 0.0.0.0:8888
+
+ # Set the network on your mobile phone to set your proxy listening address, for example: http://192.168.1.1:8888
+ # Then open the browser http://192.168.1.1:8888/preauth/cert, download the certificate, install it and trust it, then open iOS ChatGPT and you can play happily
+ ```
+
 ### Install
 
 - #### Ubuntu(Other Linux)
