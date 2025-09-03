diff --git a/README.md b/README.md
index 0da4124c..5820bde2 100644
--- a/README.md
+++ b/README.md
@@ -571,9 +571,10 @@ You can also use `$dispatch()` to trigger data updates for `x-model` bindings. F
 You can "watch" a component property with the `$watch` magic method. In the above example, when the button is clicked and `open` is changed, the provided callback will fire and `console.log` the new value.
 
 ## v3 Roadmap
-* Move from `x-ref` to `ref` for Vue parity
+* Move from `x-ref` to `ref` for Vue parity?
 * Add `Alpine.directive()`
 * Add `Alpine.component('foo', {...})` (With magic `__init()` method)
+* Dispatch Alpine events for "loaded", "transition-start", etc... (Original PR: #299) ?
 
 ## License
 
