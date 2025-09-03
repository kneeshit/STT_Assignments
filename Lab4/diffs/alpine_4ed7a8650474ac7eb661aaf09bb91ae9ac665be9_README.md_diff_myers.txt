diff --git a/README.md b/README.md
index 5bd1f523..2520b2ac 100644
--- a/README.md
+++ b/README.md
@@ -369,6 +369,11 @@ If you wish to customize this, you can specifiy a custom wait time like so:
 <input x-on:input.debounce.750ms="fetchSomething()">
 ```
 
+**`.camel` modifier**
+**Example:** `<input x-on:event-name.camel="doSomethiing()">`
+
+The `camel` modifier will attach an event listener for the camel case equivalent event name. In the example above, the expression will be evaluated when the `eventName` event is fired on the element.
+
 ---
 
 ### `x-model`
