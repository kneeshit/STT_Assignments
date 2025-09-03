diff --git a/README.ja.md b/README.ja.md
index 022dfb28..699171ac 100644
--- a/README.ja.md
+++ b/README.ja.md
@@ -14,7 +14,7 @@ DOM を保持し、適切な動作を施すことができます。
 
 **CDNより:** `<head>` セクションの最後に次のスクリプトを追加します。
 ```html
-<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.10.1/dist/alpine.js" defer></script>
+<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.6.0/dist/alpine.js" defer></script>
 ```
 
 それだけです。初期は自身で行われます。
@@ -31,9 +31,8 @@ import 'alpinejs'
 
 IE11 では、ポリフィルを提供する必要があります。次のスクリプトを上記の Alpine スクリプトの前にロードしてください。
 ```html
-<script src="https://polyfill.io/v3/polyfill.min.js?features=MutationObserver%2CArray.from%2CArray.prototype.forEach%2CMap%2CSet%2CArray.prototype.includes%2CString.prototype.includes%2CPromise%2CNodeList.prototype.forEach%2CObject.values%2CReflect%2CReflect.set"></script>
-
-<script src="https://cdn.jsdelivr.net/npm/proxy-polyfill@2.6.0/proxy.min.js"></script>
+<script type="module" src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"></script>
+<script nomodule src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine-ie11.min.js" defer></script>
 ```
 
 ## 使う
