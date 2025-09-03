diff --git a/README_zh.md b/README_zh.md
index 036c787..c7b8b84 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -3,7 +3,7 @@
 [![CI](https://github.com/gngpp/ninja/actions/workflows/CI.yml/badge.svg)](https://github.com/gngpp/ninja/actions/workflows/CI.yml)
 [![CI](https://github.com/gngpp/ninja/actions/workflows/Release.yml/badge.svg)](https://github.com/gngpp/ninja/actions/workflows/Release.yml)
  <a target="_blank" href="https://github.com/gngpp/ninja/blob/main/LICENSE">
-  <img src="https://img.shields.io/badge/license-GPL3.0-blue.svg"/>
+  <img src="https://img.shields.io/badge/license-GPL_3.0-blue.svg"/>
  </a>
   <a href="https://github.com/gngpp/ninja/releases">
     <img src="https://img.shields.io/github/release/gngpp/ninja.svg?style=flat">
@@ -48,7 +48,7 @@
 - 三种方案都使用，优先级是：`HAR` > `YesCaptcha` / `CapSolver` > `Arkose Token 端点`
 - `YesCaptcha` / `CapSolver`推荐搭配HAR使用，出验证码则调用解析器处理，验证后HAR使用更持久
 
-> 目前OpenAI已经更新登录需要验证`Arkose Token`，解决方式同GPT4，填写启动参数指定HAR文件`--arkose-auth-har-file`
+> 目前OpenAI已经更新登录需要验证`Arkose Token`，解决方式同GPT4，填写启动参数指定HAR文件`--arkose-auth-har-file`。不想上传，可以通过浏览器打码登录，非必需。
 
 ### Command Line(dev)
 
