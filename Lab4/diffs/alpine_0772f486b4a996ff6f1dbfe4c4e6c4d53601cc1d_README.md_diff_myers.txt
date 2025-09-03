diff --git a/README.md b/README.md
index 5df852bb..30ea4aab 100644
--- a/README.md
+++ b/README.md
@@ -563,12 +563,6 @@ The object keys are the directives (Can be any directive including modifiers), a
 
 > Note: The only anomoly with x-spread is when used with `x-for`. When the directive being "spread" is `x-for`, you should return a normal expression string from the callback. For example: `['x-for']() { return 'item in items' }`.
 
-```html
-<style>
-    [x-cloak] { display: none; }
-</style>
-```
-
 ---
 
 ### `x-cloak`
