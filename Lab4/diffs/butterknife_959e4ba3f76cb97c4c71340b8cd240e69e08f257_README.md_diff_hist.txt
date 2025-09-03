diff --git a/README.md b/README.md
index 714ba68..91a16af 100644
--- a/README.md
+++ b/README.md
@@ -6,7 +6,7 @@ Butter Knife
 Field and method binding for Android views which uses annotation processing to generate boilerplate
 code for you.
 
- * Eliminate `findViewById` calls by using `@Bind` on fields.
+ * Eliminate `findViewById` calls by using `@BindView` on fields.
  * Group multiple views in a list or array. Operate on all of them at once with actions,
    setters, or properties.
  * Eliminate anonymous inner-classes for listeners by annotating methods with `@OnClick` and others.
@@ -14,8 +14,8 @@ code for you.
 
 ```java
 class ExampleActivity extends Activity {
-  @Bind(R.id.user) EditText username;
-  @Bind(R.id.pass) EditText password;
+  @BindView(R.id.user) EditText username;
+  @BindView(R.id.pass) EditText password;
 
   @BindString(R.string.login_error)
   String loginErrorMessage;
