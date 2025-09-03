diff --git a/README.md b/README.md
index a83adde..59a1f06 100644
--- a/README.md
+++ b/README.md
@@ -41,39 +41,13 @@ __Remember: A butter knife is like [a dagger][1] only infinitely less sharp.__
 Download
 --------
 
-Configure your project-level `build.gradle` to include the 'android-apt' plugin:
-
 ```groovy
-buildscript {
-  repositories {
-    mavenCentral()
-   }
-  dependencies {
-    classpath 'com.neenbedankt.gradle.plugins:android-apt:1.8'
-  }
-}
-```
-
-Then, apply the 'android-apt' plugin in your module-level `build.gradle` and add the Butter Knife
-dependencies:
-
-```groovy
-apply plugin: 'android-apt'
-
-android {
-  ...
-}
-
 dependencies {
   compile 'com.jakewharton:butterknife:8.4.0'
-  apt 'com.jakewharton:butterknife-compiler:8.4.0'
+  annotationProcessor 'com.jakewharton:butterknife-compiler:8.4.0'
 }
 ```
 
-Note: If you are using the new Jack compiler with version 2.2.0 or newer you do not need the
-'android-apt' plugin and can instead replace `apt` with `annotationProcessor` when declaring the
-compiler dependency.
-
 Snapshots of the development version are available in [Sonatype's `snapshots` repository][snap].
 
 
