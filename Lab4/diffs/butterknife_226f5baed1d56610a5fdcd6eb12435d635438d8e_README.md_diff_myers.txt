diff --git a/README.md b/README.md
index d6ca7af..bccd315 100644
--- a/README.md
+++ b/README.md
@@ -41,6 +41,8 @@ __Remember: A butter knife is like [a dagger][1] only infinitely less sharp.__
 Download
 --------
 
+Add this to you project-level `build.gradle`:
+
 ```groovy
 buildscript {
   repositories {
@@ -50,8 +52,16 @@ buildscript {
     classpath 'com.neenbedankt.gradle.plugins:android-apt:1.8'
   }
 }
+```
 
-apply plugin: 'com.neenbedankt.android-apt'
+Add this to your module-level `build.gradle`:
+
+```groovy
+apply plugin: 'android-apt'
+
+android {
+  ...
+}
 
 dependencies {
   compile 'com.jakewharton:butterknife:8.0.1'
@@ -59,6 +69,8 @@ dependencies {
 }
 ```
 
+Make sure the line `apply plugin ...` is placed somewhere at the top of the file.
+
 Snapshots of the development version are available in [Sonatype's `snapshots` repository][snap].
 
 
