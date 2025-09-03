diff --git a/README.md b/README.md
index 7aeda23..cb56dd0 100644
--- a/README.md
+++ b/README.md
@@ -41,7 +41,7 @@ __Remember: A butter knife is like [a dagger][1] only infinitely less sharp.__
 Download
 --------
 
-Add this to you project-level `build.gradle`:
+Configure your project-level `build.gradle` to include the 'android-apt' plugin:
 
 ```groovy
 buildscript {
@@ -54,7 +54,8 @@ buildscript {
 }
 ```
 
-Add this to your module-level `build.gradle`:
+Then, apply the 'android-apt' plugin in your module-level `build.gradle` and add the Butter Knife
+dependencies:
 
 ```groovy
 apply plugin: 'android-apt'
@@ -69,11 +70,42 @@ dependencies {
 }
 ```
 
-Make sure the line `apply plugin ...` is placed somewhere at the top of the file.
-
 Snapshots of the development version are available in [Sonatype's `snapshots` repository][snap].
 
 
+
+Library projects
+--------------------
+
+To use Butter Knife in a library, add the plugin to your `buildscript`:
+
+```groovy
+buildscript {
+  dependencies {
+    classpath 'com.jakewharton:butterknife-gradle-plugin:8.2.0' // Only needed for android libraries
+  }
+}
+```
+
+and then apply it in your module:
+
+```groovy
+apply plugin: 'com.android.library'
+apply plugin: 'com.jakewharton.butterknife'
+```
+
+Now make sure you to use `R2` instead of `R` inside all Butter Knife annotations.
+
+```java
+class ExampleActivity extends Activity {
+  @BindView(R2.id.user) EditText username;
+  @BindView(R2.id.pass) EditText password;
+...
+}
+```
+
+
+
 License
 -------
 
