diff --git a/README.md b/README.md
index d546612a..41a58d7a 100644
--- a/README.md
+++ b/README.md
@@ -32,8 +32,6 @@ Include it in your script.
 import 'alpinejs'
 ```
 
-**For bundler users**, note that Alpine.js accesses functions that are in the global scope (`window`), you'll need to explicitly assign your functions to `window` in order to use them with `x-data` for example `window.dropdown = function () {}` (this is because with Webpack, Rollup, Parcel etc. `function`'s you define will default to the module's scope not `window`).
-
 **For IE11 support** Use the following script instead.
 ```html
 <script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine-ie11.min.js" defer></script>
@@ -156,6 +154,9 @@ You can extract data (and behavior) into reusable functions:
 </script>
 ```
 
+**For bundler users**, note that Alpine.js accesses functions that are in the global scope (`window`), you'll need to explicitly assign your functions to `window` in order to use them with `x-data` for example `window.dropdown = function () {}` (this is because with Webpack, Rollup, Parcel etc. `function`'s you define will default to the module's scope not `window`).
+
+
 You can also mix-in multiple data objects using object destructuring:
 
 ```html
