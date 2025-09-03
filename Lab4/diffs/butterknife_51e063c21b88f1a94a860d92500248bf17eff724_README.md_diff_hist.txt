diff --git a/README.md b/README.md
index 13e77fd..7e1a9aa 100644
--- a/README.md
+++ b/README.md
@@ -41,34 +41,6 @@ __Remember: A butter knife is like [a dagger][1] only infinitely less sharp.__
 Download
 --------
 
-Download [the latest JAR][2] or grab via Maven:
-```xml
-<dependency>
-  <groupId>com.jakewharton</groupId>
-  <artifactId>butterknife</artifactId>
-  <version>7.0.1</version>
-</dependency>
-```
-or Gradle:
-```groovy
-compile 'com.jakewharton:butterknife:7.0.1'
-```
-
-For the SNAPSHOT version:
-```xml
-<dependency>
-  <groupId>com.jakewharton</groupId>
-  <artifactId>butterknife</artifactId>
-  <version>8.0.0-SNAPSHOT</version>
-</dependency>
-<dependency>
-  <groupId>com.jakewharton</groupId>
-  <artifactId>butterknife-compiler</artifactId>
-  <version>8.0.0-SNAPSHOT</version>
-  <optional>true</optional>
-</dependency>
-```
-or Gradle:
 ```groovy
 buildscript {
   dependencies {
@@ -76,18 +48,11 @@ buildscript {
   }
 }
 
-allprojects {
-  repositories {
-    maven { url "https://oss.sonatype.org/content/repositories/snapshots" }
-  }
-}
-```
-```groovy
 apply plugin: 'com.neenbedankt.android-apt'
 
 dependencies {
-  compile 'com.jakewharton:butterknife:8.0.0-SNAPSHOT'
-  apt 'com.jakewharton:butterknife-compiler:8.0.0-SNAPSHOT'
+  compile 'com.jakewharton:butterknife:8.0.0'
+  apt 'com.jakewharton:butterknife-compiler:8.0.0'
 }
 ```
 
