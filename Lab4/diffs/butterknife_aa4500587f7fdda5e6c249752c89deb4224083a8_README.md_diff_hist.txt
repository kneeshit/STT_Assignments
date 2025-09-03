diff --git a/README.md b/README.md
index 3199810..417d8ff 100644
--- a/README.md
+++ b/README.md
@@ -49,31 +49,39 @@ Download [the latest JAR][2] or grab via Maven:
   <artifactId>butterknife</artifactId>
   <version>7.0.1</version>
 </dependency>
+```
+or Gradle:
+```groovy
+compile 'com.jakewharton:butterknife:7.0.1'
+```
+
+For the SNAPSHOT version:
+```xml
+<dependency>
+  <groupId>com.jakewharton</groupId>
+  <artifactId>butterknife</artifactId>
+  <version>7.0.2-SNAPSHOT</version>
+</dependency>
 <dependency>
   <groupId>com.jakewharton</groupId>
   <artifactId>butterknife-compiler</artifactId>
-  <version>7.0.1</version>
+  <version>7.0.2-SNAPSHOT</version>
   <optional>true</optional>
 </dependency>
 ```
 or Gradle:
 ```groovy
 buildscript {
-  repositories {
-    mavenCentral()
-  }
-
   dependencies {
-    // ...
     classpath 'com.neenbedankt.gradle.plugins:android-apt:1.6'
   }
 }
 
-// ...
+apply plugin: 'com.neenbedankt.android-apt'
 
 dependencies {
-  compile 'com.jakewharton:butterknife:7.0.1'
-  apt 'com.jakewharton:butterknife-compiler:7.0.1'
+  compile 'com.jakewharton:butterknife:7.0.2-SNAPSHOT'
+  apt 'com.jakewharton:butterknife-compiler:7.0.2-SNAPSHOT'
 }
 ```
 
