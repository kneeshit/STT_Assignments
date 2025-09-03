diff --git a/README.md b/README.md
index fba69602..99d45120 100644
--- a/README.md
+++ b/README.md
@@ -180,6 +180,12 @@ If you wish to run code AFTER Alpine has made its initial updates to the DOM (so
 
 `x-show` toggles the `display: none;` style on the element depending if the expression resolves to `true` or `false`.
 
+> Note: `x-show` will wait for any children to finish transitioning out. If you want to bypass this behavior, add the `.immediate` modifer:
+```html
+<div x-show.immediate="open">
+    <div x-show="open" x-transition:leave="transition-out">
+</div>
+```
 ---
 
 ### `x-bind`
