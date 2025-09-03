diff --git a/README.md b/README.md
index 5df852bb..27d0ca45 100644
--- a/README.md
+++ b/README.md
@@ -561,7 +561,7 @@ These behave exactly like VueJs's transition directives, except they have differ
 
 The object keys are the directives (Can be any directive including modifiers), and the values are callbacks to be evaluated by Alpine.
 
-> Note: The only anomoly with x-spread is when used with `x-for`. When the directive being "spread" is `x-for`, you should return a normal expression string from the callback. For example: `['x-for']() { return 'item in items' }`.
+> Note: The only anomaly with x-spread is when used with `x-for`. When the directive being "spread" is `x-for`, you should return a normal expression string from the callback. For example: `['x-for']() { return 'item in items' }`.
 
 ```html
 <style>
