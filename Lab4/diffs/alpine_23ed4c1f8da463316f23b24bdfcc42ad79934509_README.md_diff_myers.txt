diff --git a/README.md b/README.md
index 4e160186..69053eac 100644
--- a/README.md
+++ b/README.md
@@ -22,6 +22,12 @@ Think of it like [Tailwind](https://tailwindcss.com/) for JavaScript.
 
 That's it. It will initialize itself.
 
+For production environments, it's recommend linking to a specific version number to avoid unexpected breakage from newer versions. 
+For example, to use version `2.3.5`:
+```html
+<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.3.5/dist/alpine.min.js" defer></script>
+```
+
 **From NPM:** Install the package from NPM.
 ```js
 npm i alpinejs
