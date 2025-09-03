diff --git a/README.md b/README.md
index c096bc4..a923372 100644
--- a/README.md
+++ b/README.md
@@ -8,9 +8,12 @@ generate code that does direct field assignment of your views.
 
 ```java
 class ExampleActivity extends Activity {
-  @InjectView(R.id.title) TextView title;
-  @InjectView(R.id.subtitle) TextView subtitle;
-  @InjectView(R.id.footer) TextView footer;
+  @InjectView(R.id.user) EditText username;
+  @InjectView(R.id.pass) EditText password;
+
+  @OnClick(R.id.submit) void submit() {
+    // TODO call server...
+  }
 
   @Override public void onCreate(Bundle savedInstanceState) {
     super.onCreate(savedInstanceState);
