diff --git a/README.md b/README.md
index 91a16af..13e77fd 100644
--- a/README.md
+++ b/README.md
@@ -17,8 +17,7 @@ class ExampleActivity extends Activity {
   @BindView(R.id.user) EditText username;
   @BindView(R.id.pass) EditText password;
 
-  @BindString(R.string.login_error)
-  String loginErrorMessage;
+  @BindString(R.string.login_error) String loginErrorMessage;
 
   @OnClick(R.id.submit) void submit() {
     // TODO call server...
