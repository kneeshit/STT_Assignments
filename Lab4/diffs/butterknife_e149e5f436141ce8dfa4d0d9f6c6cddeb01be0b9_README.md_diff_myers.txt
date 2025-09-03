diff --git a/README.md b/README.md
index a94b2d6..d244d57 100644
--- a/README.md
+++ b/README.md
@@ -24,7 +24,8 @@ class ExampleActivity extends Activity {
     title = (TextView) findViewById(R.id.title);
     subtitle = (TextView) findViewById(R.id.subtitle);
     footer = (TextView) findViewById(R.id.footer);
-    // ...
+
+    // TODO Use views...
   }
 }
 ```
@@ -42,7 +43,7 @@ class ExampleActivity extends Activity {
   @Override public void onCreate(Bundle savedInstanceState) {
     super.onCreate(savedInstanceState);
     setContentView(R.layout.simple_activity);
-    // ...
+    // TODO Use "injected" views...
   }
 }
 ```
@@ -64,7 +65,7 @@ class ExampleActivity extends Activity {
     super.onCreate(savedInstanceState);
     setContentView(R.layout.simple_activity);
     Views.inject(this);
-    // ...
+    // TODO Use "injected" views...
   }
 }
 ```
@@ -81,14 +82,68 @@ public void inject(ExampleActivity activity) {
 ```
 
 Some people call this view injection and lump it along with traditional
-dependency injection frameworks. They are wrong in nomenclature, but perhaps
-there exists some necessity for this terseness.
+dependency injection frameworks. They may be wrong in nomenclature, but perhaps
+there exists some use for this type of field assignment.
 
 __Remember: A butter knife is like [a dagger][1] only infinitely less sharp.__
 
 *Do not take this library too seriously, but it may be useful for some things.*
 
 
+Non-Activity Injection
+----------------------
+
+You can also perform injection on arbitrary objects by supplying your own view
+root.
+
+```java
+public class FancyFragment extends Fragment {
+  @InjectView(R.id.button1) Button button1;
+  @InjectView(R.id.button2) Button button2;
+
+  @Override View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
+    View view = inflater.inflate(R.layout.fancy_fragment, container, false);
+    Views.inject(this, view);
+    // TODO Use "injected" views...
+    return view;
+  }
+}
+```
+
+Another use is simplifying the view holder pattern inside of a list adapter.
+
+```java
+public class MyAdapter extends BaseAdapter {
+  @Override public void getView(int position, View view, ViewGroup parent) {
+    ViewHolder holder;
+    if (view != null) {
+      holder = (ViewHolder) view.getTag();
+    } else {
+      view = inflater.inflate(R.layout.whatever, parent, false);
+      holder = new ViewHolder(view);
+      view.setTag(holder);
+    }
+
+    holder.name.setText("John Doe");
+    // etc...
+
+    return convertView;
+  }
+
+  static class ViewHolder {
+    @InjectView(R.id.title) TextView name;
+    @InjectView(R.id.job_title) TextView jobTitle;
+
+    public ViewHolder(View view) {
+      Views.inject(this, view);
+    }
+  }
+}
+```
+
+You can see this implementation in action in the provided sample.
+
+
 
 Bonus
 -----
