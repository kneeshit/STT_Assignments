diff --git a/README.md b/README.md
index 23c1db2..a28623a 100644
--- a/README.md
+++ b/README.md
@@ -18,7 +18,7 @@ class ExampleActivity extends Activity {
   @Override public void onCreate(Bundle savedInstanceState) {
     super.onCreate(savedInstanceState);
     setContentView(R.layout.simple_activity);
-    Views.inject(this);
+    ButterKnife.inject(this);
     // TODO Use "injected" views...
   }
 }
