diff --git a/README.md b/README.md
index dbbcf19..714ba68 100644
--- a/README.md
+++ b/README.md
@@ -77,6 +77,13 @@ buildscript {
   }
 }
 
+allprojects {
+  repositories {
+    maven { url "https://oss.sonatype.org/content/repositories/snapshots" }
+  }
+}
+```
+```groovy
 apply plugin: 'com.neenbedankt.android-apt'
 
 dependencies {
