diff --git a/README.md b/README.md
index cc97921..b18cb7f 100644
--- a/README.md
+++ b/README.md
@@ -141,13 +141,24 @@ public class MyAdapter extends BaseAdapter {
 
 You can see this implementation in action in the provided sample.
 
+Other provided injection APIs:
+
+ * Inject arbitrary objects using an activity as the view root. If you use a
+   pattern like MVC you can inject the controller using its activity with
+   `Views.inject(this, activity)`.
+ * Inject a view's children into fields using `Views.inject(this)`. If you use
+   `<merge>` tags in a layout and inflate in a custom view constructor you can
+   call this immediately after. Alternatively, custom view types inflated from
+   XML can use it in the `onLayoutInflated()` callback.
+
 
 
 Bonus
 -----
 
-Also included is a helper method for simplifying code which still has to call
-`findViewById` on either a `View` or `Activity`:
+Also included are two `findById` methods which simplify code that still has to
+find views on a `View` or `Activity`. It uses generics to infer the return type
+and automatically performs the cast.
 
 ```java
 View view = LayoutInflater.from(context).inflate(R.layout.thing, null);
