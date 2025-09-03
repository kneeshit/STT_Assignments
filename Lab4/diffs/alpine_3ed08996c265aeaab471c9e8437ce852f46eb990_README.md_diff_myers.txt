diff --git a/README.md b/README.md
index 2dc4a792..1e7cf5c0 100644
--- a/README.md
+++ b/README.md
@@ -14,6 +14,13 @@ Add the following script to the end of your `<head>` section.
 <script src="https://cdn.jsdelivr.net/gh/calebporzio/project-x@v0.4.0/dist/project-x.min.js" defer></script>
 ```
 
+For IE11, polyfills will need to be provided. Please load the following scripts before the project-x script above.
+```html 
+<script src="https://polyfill.io/v3/polyfill.min.js?features=MutationObserver%2CArray.from%2CArray.prototype.forEach%2CMap%2CSet%2CArray.prototype.includes%2CString.prototype.includes%2CPromise%2CNodeList.prototype.forEach%2CObject.values%2CReflect%2CReflect.set"></script>
+
+<script src="https://cdn.jsdelivr.net/npm/proxy-polyfill@0.3.0/proxy.min.js"></script>
+```
+
 ## Use
 
 *Dropdown/Modal*
