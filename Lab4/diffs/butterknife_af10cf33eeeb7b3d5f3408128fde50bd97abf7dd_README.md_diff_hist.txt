diff --git a/butterknife-reflect/README.md b/butterknife-reflect/README.md
index 8cfb858..a4f06e8 100644
--- a/butterknife-reflect/README.md
+++ b/butterknife-reflect/README.md
@@ -34,10 +34,10 @@ Kotlin modules:
 ```groovy
 dependencies {
   if (properties.containsKey('android.injected.invoked.from.ide')) {
-    implementation 'com.jakewharton.butterknife:butterknife-reflect:<version>'
+    implementation 'com.jakewharton:butterknife-reflect:<version>'
   } else {
-    implementation 'com.jakewharton.butterknife:butterknife:<version>'
-    kapt 'com.jakewharton.butterknife:butterknife-compiler:<version>'
+    implementation 'com.jakewharton:butterknife:<version>'
+    kapt 'com.jakewharton:butterknife-compiler:<version>'
   }
 }
 ```
@@ -46,10 +46,10 @@ Java modules:
 ```groovy
 dependencies {
   if (properties.containsKey('android.injected.invoked.from.ide')) {
-    implementation 'com.jakewharton.butterknife:butterknife-reflect:<version>'
+    implementation 'com.jakewharton:butterknife-reflect:<version>'
   } else {
-    implementation 'com.jakewharton.butterknife:butterknife:<version>'
-    annotationProcessor 'com.jakewharton.butterknife:butterknife-compiler:<version>'
+    implementation 'com.jakewharton:butterknife:<version>'
+    annotationProcessor 'com.jakewharton:butterknife-compiler:<version>'
   }
 }
 ```
