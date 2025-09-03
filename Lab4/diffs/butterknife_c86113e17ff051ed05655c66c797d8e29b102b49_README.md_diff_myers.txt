diff --git a/README.md b/README.md
index 417d8ff..4d8ef3e 100644
--- a/README.md
+++ b/README.md
@@ -60,12 +60,12 @@ For the SNAPSHOT version:
 <dependency>
   <groupId>com.jakewharton</groupId>
   <artifactId>butterknife</artifactId>
-  <version>7.0.2-SNAPSHOT</version>
+  <version>8.0.0-SNAPSHOT</version>
 </dependency>
 <dependency>
   <groupId>com.jakewharton</groupId>
   <artifactId>butterknife-compiler</artifactId>
-  <version>7.0.2-SNAPSHOT</version>
+  <version>8.0.0-SNAPSHOT</version>
   <optional>true</optional>
 </dependency>
 ```
@@ -80,8 +80,8 @@ buildscript {
 apply plugin: 'com.neenbedankt.android-apt'
 
 dependencies {
-  compile 'com.jakewharton:butterknife:7.0.2-SNAPSHOT'
-  apt 'com.jakewharton:butterknife-compiler:7.0.2-SNAPSHOT'
+  compile 'com.jakewharton:butterknife:8.0.0-SNAPSHOT'
+  apt 'com.jakewharton:butterknife-compiler:8.0.0-SNAPSHOT'
 }
 ```
 
