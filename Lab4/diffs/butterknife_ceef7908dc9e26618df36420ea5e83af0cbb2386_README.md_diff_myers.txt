diff --git a/README.md b/README.md
index a28623a..fc48ff1 100644
--- a/README.md
+++ b/README.md
@@ -3,8 +3,13 @@ Butter Knife
 
 ![Logo](website/static/logo.png)
 
-View "injection" library for Android which uses annotation processing to
-generate code that does direct field assignment of your views.
+View "injection" library for Android which uses annotation processing to generate boilerplate code
+for you.
+
+ * Eliminate `findViewById` calls by using `@InjectView` on fields.
+ * Group multiple views in a list using `@InjectViews`. Operate on all of them at once with actions,
+   setters, or properties.
+ * Eliminate anonymous inner-classes for listeners by annotating methods with `@OnClick` and others.
 
 ```java
 class ExampleActivity extends Activity {
