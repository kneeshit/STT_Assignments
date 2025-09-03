diff --git a/README.md b/README.md
index 41a58d7a..6d645f8d 100644
--- a/README.md
+++ b/README.md
@@ -154,7 +154,7 @@ You can extract data (and behavior) into reusable functions:
 </script>
 ```
 
-**For bundler users**, note that Alpine.js accesses functions that are in the global scope (`window`), you'll need to explicitly assign your functions to `window` in order to use them with `x-data` for example `window.dropdown = function () {}` (this is because with Webpack, Rollup, Parcel etc. `function`'s you define will default to the module's scope not `window`).
+> **For bundler users**, note that Alpine.js accesses functions that are in the global scope (`window`), you'll need to explicitly assign your functions to `window` in order to use them with `x-data` for example `window.dropdown = function () {}` (this is because with Webpack, Rollup, Parcel etc. `function`'s you define will default to the module's scope not `window`).
 
 
 You can also mix-in multiple data objects using object destructuring:
