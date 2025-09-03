diff --git a/README.md b/README.md
index 0ab74aae..8c296074 100644
--- a/README.md
+++ b/README.md
@@ -9,11 +9,26 @@ Think of it like [Tailwind](https://tailwindcss.com/) for JavaScript.
 > Note: This tool's syntax is almost entirely borrowed from [Vue.js](https://vuejs.org/)(and by extension [Angular](https://angularjs.org/)). I am forever grateful for the gift they are to the web.
 
 ## Install
+
+**From CDN**
 Add the following script to the end of your `<head>` section.
 ```html
 <script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.0.0/dist/alpine.min.js" defer></script>
 ```
 
+**From NPM**
+Install the package from NPM.
+```js
+npm i alpinejs
+```
+
+Include, and start it in your scripts:
+```js
+import Alpine from 'alpinejs'
+
+Alpine.start()
+```
+
 ## Use
 
 *Dropdown/Modal*
