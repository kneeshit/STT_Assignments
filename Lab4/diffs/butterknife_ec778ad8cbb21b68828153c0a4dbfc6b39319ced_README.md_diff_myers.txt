diff --git a/README.md b/README.md
index 5f82476..a27fe2d 100644
--- a/README.md
+++ b/README.md
@@ -3,18 +3,18 @@ Butter Knife
 
 ![Logo](website/static/logo.png)
 
-View "injection" library for Android which uses annotation processing to generate boilerplate code
-for you.
+Field and method binding for Android views which uses annotation processing to generate boilerplate
+code for you.
 
- * Eliminate `findViewById` calls by using `@InjectView` on fields.
- * Group multiple views in a list using `@InjectViews`. Operate on all of them at once with actions,
+ * Eliminate `findViewById` calls by using `@FindView` on fields.
+ * Group multiple views in a list using `@FindViews`. Operate on all of them at once with actions,
    setters, or properties.
  * Eliminate anonymous inner-classes for listeners by annotating methods with `@OnClick` and others.
 
 ```java
 class ExampleActivity extends Activity {
-  @InjectView(R.id.user) EditText username;
-  @InjectView(R.id.pass) EditText password;
+  @FindView(R.id.user) EditText username;
+  @FindView(R.id.pass) EditText password;
 
   @OnClick(R.id.submit) void submit() {
     // TODO call server...
@@ -23,8 +23,8 @@ class ExampleActivity extends Activity {
   @Override public void onCreate(Bundle savedInstanceState) {
     super.onCreate(savedInstanceState);
     setContentView(R.layout.simple_activity);
-    ButterKnife.inject(this);
-    // TODO Use "injected" views...
+    ButterKnife.bind(this);
+    // TODO Use fields...
   }
 }
 ```
