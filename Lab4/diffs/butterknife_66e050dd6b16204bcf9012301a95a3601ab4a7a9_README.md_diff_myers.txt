diff --git a/README.md b/README.md
index 659df84..3199810 100644
--- a/README.md
+++ b/README.md
@@ -49,10 +49,32 @@ Download [the latest JAR][2] or grab via Maven:
   <artifactId>butterknife</artifactId>
   <version>7.0.1</version>
 </dependency>
+<dependency>
+  <groupId>com.jakewharton</groupId>
+  <artifactId>butterknife-compiler</artifactId>
+  <version>7.0.1</version>
+  <optional>true</optional>
+</dependency>
 ```
 or Gradle:
 ```groovy
+buildscript {
+  repositories {
+    mavenCentral()
+  }
+
+  dependencies {
+    // ...
+    classpath 'com.neenbedankt.gradle.plugins:android-apt:1.6'
+  }
+}
+
+// ...
+
+dependencies {
   compile 'com.jakewharton:butterknife:7.0.1'
+  apt 'com.jakewharton:butterknife-compiler:7.0.1'
+}
 ```
 
 Snapshots of the development version are available in [Sonatype's `snapshots` repository][snap].
