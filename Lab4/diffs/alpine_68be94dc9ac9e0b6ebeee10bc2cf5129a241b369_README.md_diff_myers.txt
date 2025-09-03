diff --git a/README.md b/README.md
index 15525b15..a44fbfe6 100644
--- a/README.md
+++ b/README.md
@@ -29,6 +29,8 @@ Include it in your script.
 import 'alpinejs'
 ```
 
+**For bundler users**, note that Alpine.js accesses functions that are in the global scope (`window`), you'll need to explicitly assign your functions to `window` for example `window.dropdown = function () {}` since with Webpack, Rollup, Parcel etc. `function`'s you define will default to module scope.
+
 **For IE11 support** Use the following script instead.
 ```html
 <script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine-ie11.js" defer></script>
