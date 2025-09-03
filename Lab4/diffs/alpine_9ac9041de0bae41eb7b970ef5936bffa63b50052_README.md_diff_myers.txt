diff --git a/README.md b/README.md
index 1ba4803a..1cd9c41c 100644
--- a/README.md
+++ b/README.md
@@ -12,7 +12,7 @@ Think of it like [Tailwind](https://tailwindcss.com/) for JavaScript.
 
 **From CDN:** Add the following script to the end of your `<head>` section.
 ```html
-<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.1.1/dist/alpine.min.js" defer></script>
+<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.1.2/dist/alpine.umd.js" defer></script>
 ```
 
 That's it. It will initialize itself.
@@ -22,11 +22,9 @@ That's it. It will initialize itself.
 npm i alpinejs
 ```
 
-Include, and start it in your scripts:
+Include it in your script.
 ```js
 import Alpine from 'alpinejs'
-
-Alpine.start()
 ```
 
 For IE11, polyfills will need to be provided. Please load the following scripts before the Alpine script above.
