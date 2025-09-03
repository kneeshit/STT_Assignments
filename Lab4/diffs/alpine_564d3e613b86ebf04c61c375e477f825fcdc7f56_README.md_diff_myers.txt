diff --git a/README.md b/README.md
index b0b16ea6..a48f7781 100644
--- a/README.md
+++ b/README.md
@@ -301,7 +301,7 @@ Boolean attributes are supported as per the [HTML specification](https://html.sp
 
 If any data is modified in the expression, other element attributes "bound" to this data, will be updated.
 
-> Note: You can also specify a Javascript function name
+> Note: You can also specify a JavaScript function name
 
 **Example:** `<button x-on:click="myFunction"></button>`
 
@@ -568,7 +568,7 @@ These behave exactly like VueJs's transition directives, except they have differ
 
 `$event` is a magic property that can be used within an event listener to retrieve the native browser "Event" object.
 
-> Note: The $event property is only available in the DOM.
+> Note: The $event property is only available in DOM expressions.
 
 If you need to access $event inside of a JavaScript function you can pass it in directly:
 
@@ -600,7 +600,7 @@ You can also use `$dispatch()` to trigger data updates for `x-model` bindings. F
 </div>
 ```
 
-> Note: The $dispatch property is only available in the DOM.
+> Note: The $dispatch property is only available in DOM expressions.
 
 If you need to access $dispatch inside of a JavaScript function you can pass it in directly:
 
