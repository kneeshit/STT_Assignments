diff --git a/README.md b/README.md
index 42ed5ce9..585ea0bd 100644
--- a/README.md
+++ b/README.md
@@ -29,13 +29,9 @@ Include it in your script.
 import 'alpinejs'
 ```
 
-For IE11, a different Alpine script is used and polyfills need to be provided. Please add the following scripts to the end of your `<head>`> section.
+**For IE11** Please use this script instead. Add the following script to the end of your `<head>`> section.
 ```html
-<script src="https://polyfill.io/v3/polyfill.js?features=MutationObserver%2CArray.from%2CArray.prototype.forEach%2CMap%2CSet%2CArray.prototype.includes%2CString.prototype.includes%2CPromise%2CNodeList.prototype.forEach%2CObject.values%2CReflect%2CReflect.set%2CString.prototype.startsWith%2CArray.prototype.find%2CArray.prototype.findIndex%2CElement.prototype.closest%2CElement.prototype.remove%2CCustomEvent%2CElement.prototype.classList%2CHTMLTemplateElement"></script>
-<script src="https://unpkg.com/shim-selected-options"></script>
-<script src="https://cdn.jsdelivr.net/npm/proxy-polyfill@0.3.0/proxy.min.js"></script>
-
-<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.9.8/dist/alpine_ie11.js" defer></script>
+<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.10.1/dist/alpine_ie11.js" defer></script>
 ```
 
 
