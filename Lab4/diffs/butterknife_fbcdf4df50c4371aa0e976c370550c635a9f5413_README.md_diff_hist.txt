diff --git a/README.md b/README.md
index d6014c2..ad45d26 100644
--- a/README.md
+++ b/README.md
@@ -65,8 +65,8 @@ android {
 }
 
 dependencies {
-  compile 'com.jakewharton:butterknife:8.1.0'
-  apt 'com.jakewharton:butterknife-compiler:8.1.0'
+  compile 'com.jakewharton:butterknife:8.2.0'
+  apt 'com.jakewharton:butterknife-compiler:8.2.0'
 }
 ```
 
@@ -86,7 +86,7 @@ To use Butter Knife in a library, add the plugin to your `buildscript`:
 ```groovy
 buildscript {
   dependencies {
-    classpath 'com.jakewharton:butterknife-gradle-plugin:8.2.0' // Only needed for android libraries
+    classpath 'com.jakewharton:butterknife-gradle-plugin:8.2.0'
   }
 }
 ```
