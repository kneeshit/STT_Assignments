diff --git a/README.md b/README.md
index 07d369a3..57e60156 100644
--- a/README.md
+++ b/README.md
@@ -17,14 +17,11 @@ Think of it like [Tailwind](https://tailwindcss.com/) for JavaScript.
 
 **From CDN:** Add the following script to the end of your `<head>` section.
 ```html
-<script type="module" src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"></script>
-<script nomodule src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine-ie11.min.js" defer></script>
+<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script>
 ```
 
 That's it. It will initialize itself.
 
-The pattern above is the [module/nomodule pattern](https://philipwalton.com/articles/deploying-es2015-code-in-production-today/) that will result in the modern bundle automatically loaded on modern browsers, and the IE11 bundle loaded automatically on IE11 and other legacy browsers. 
-
 **From NPM:** Install the package from NPM.
 ```js
 npm i alpinejs
@@ -35,6 +32,14 @@ Include it in your script.
 import 'alpinejs'
 ```
 
+**For IE11 support** Use the following scripts instead.
+```html
+<script type="module" src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"></script>
+<script nomodule src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine-ie11.min.js" defer></script>
+```
+
+The pattern above is the [module/nomodule pattern](https://philipwalton.com/articles/deploying-es2015-code-in-production-today/) that will result in the modern bundle automatically loaded on modern browsers, and the IE11 bundle loaded automatically on IE11 and other legacy browsers.
+
 ## Use
 
 *Dropdown/Modal*
