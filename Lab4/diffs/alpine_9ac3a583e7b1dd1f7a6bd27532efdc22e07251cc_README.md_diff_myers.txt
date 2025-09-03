diff --git a/README.md b/README.md
index 30703c90..a11f11a9 100644
--- a/README.md
+++ b/README.md
@@ -275,6 +275,12 @@ Boolean attributes are supported as per the [HTML specification](https://html.sp
 
 If any data is modified in the expression, other element attributes "bound" to this data, will be updated.
 
+> Note: You can also specify a Javascript function name
+
+**Example:** `<button x-on:click="myFunction"></button>`
+
+This is equivalent to: `<button x-on:click="myFunction($event)"></button>`
+
 **`keydown` modifiers**
 
 **Example:** `<input type="text" x-on:keydown.escape="open = false">`
@@ -536,6 +542,12 @@ These behave exactly like VueJs's transition directives, except they have differ
 
 `$event` is a magic property that can be used within an event listener to retrieve the native browser "Event" object.
 
+> Note: The $event property is only available in the DOM.
+
+If you need to access $event inside of a Javascript function you can pass it in directly:
+
+`<button x-on:click="myFunction($event)"></button>`
+
 ---
 
 ### `$dispatch`
@@ -562,6 +574,12 @@ You can also use `$dispatch()` to trigger data updates for `x-model` bindings. F
 </div>
 ```
 
+> Note: The $dispatch property is only available in the DOM.
+
+If you need to access $dispatch inside of a Javascript function you can pass it in directly:
+
+`<button x-on:click="myFunction($dispatch)"></button>`
+
 ---
 
 ### `$nextTick`
