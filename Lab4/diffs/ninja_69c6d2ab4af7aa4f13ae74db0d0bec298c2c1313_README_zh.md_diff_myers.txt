diff --git a/README_zh.md b/README_zh.md
index 2850d46..1b42b70 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -95,6 +95,16 @@
 
 `关于Refresh Token`获取的方式，采用`Apple`平台`ChatGPT App`登录方式，原理是使用内置MITM代理。`Apple设备`连上代理即可开启`Apple平台`登录获取`RefreshToken`，仅适用于量小或者个人使用`（量大会封设备，慎用）`，详细使用请看启动参数说明。
 
+```shell
+# 生成证书
+ninja genca
+
+ninja run --pbind 0.0.0.0:8888
+
+# 手机设置网络设置你代理监听地址，例如： http://192.168.1.1:8888
+# 之后浏览器打开 http://192.168.1.1：8888/preauth/cert，下载证书安装并信任，之后打开iOS ChatGPT就可以愉快玩耍了
+```
+
 
 ### 安装
 
