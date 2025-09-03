diff --git a/README.md b/README.md
index 6adf585..26e7abe 100644
--- a/README.md
+++ b/README.md
@@ -3,7 +3,7 @@
 [![CI](https://github.com/gngpp/ninja/actions/workflows/CI.yml/badge.svg)](https://github.com/gngpp/ninja/actions/workflows/CI.yml)
 [![CI](https://github.com/gngpp/ninja/actions/workflows/Release.yml/badge.svg)](https://github.com/gngpp/ninja/actions/workflows/Release.yml)
  <a target="_blank" href="https://github.com/gngpp/ninja/blob/main/LICENSE">
-  <img src="https://img.shields.io/badge/license-GPL3.0-blue.svg"/>
+  <img src="https://img.shields.io/badge/license-GPL_3.0-blue.svg"/>
  </a>
   <a href="https://github.com/gngpp/ninja/releases">
     <img src="https://img.shields.io/github/release/gngpp/ninja.svg?style=flat">
@@ -48,7 +48,7 @@ Sending a `GPT4` conversation requires `Arkose Token` to be sent as a parameter,
 - All three solutions are used, the priority is: `HAR` > `YesCaptcha/CapSolver` > `Arkose Token endpoint`
 - `YesCaptcha/CapSolver` is recommended to be used with HAR. When the verification code is generated, the parser is called for processing. After verification, HAR is more durable.
 
-> Currently OpenAI has updated that login requires verification of `Arkose Token`. The solution is the same as GPT4. Fill in the startup parameters and specify the HAR file `--arkose-auth-har-file`
+> Currently OpenAI has updated that login requires verification of `Arkose Token`. The solution is the same as GPT4. Fill in the startup parameters and specify the HAR file `--arkose-auth-har-file`. If you don't want to upload, you can log in through the browser code, which is not required.
 
 ### Command Line(dev)
 
