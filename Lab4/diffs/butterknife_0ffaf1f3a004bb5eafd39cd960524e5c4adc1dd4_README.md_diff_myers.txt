diff --git a/README.md b/README.md
index a27fe2d..300e2a8 100644
--- a/README.md
+++ b/README.md
@@ -6,15 +6,19 @@ Butter Knife
 Field and method binding for Android views which uses annotation processing to generate boilerplate
 code for you.
 
- * Eliminate `findViewById` calls by using `@FindView` on fields.
- * Group multiple views in a list using `@FindViews`. Operate on all of them at once with actions,
+ * Eliminate `findViewById` calls by using `@BindView` on fields.
+ * Group multiple views in a list using `@BindViews`. Operate on all of them at once with actions,
    setters, or properties.
  * Eliminate anonymous inner-classes for listeners by annotating methods with `@OnClick` and others.
+ * Eliminate resource lookups by using resource annotations on fields.
 
 ```java
 class ExampleActivity extends Activity {
-  @FindView(R.id.user) EditText username;
-  @FindView(R.id.pass) EditText password;
+  @BindView(R.id.user) EditText username;
+  @BindView(R.id.pass) EditText password;
+
+  @BindString(R.string.login_error)
+  String loginErrorMessage;
 
   @OnClick(R.id.submit) void submit() {
     // TODO call server...
