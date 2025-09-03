diff --git a/README.md b/README.md
index bb6af820..99e1ab4d 100644
--- a/README.md
+++ b/README.md
@@ -170,7 +170,7 @@ You can also mix-in multiple data objects using object destructuring:
 
 If you wish to run code AFTER Alpine has made its initial updates to the DOM (something like a `mounted()` hook in VueJS), you can return a callback from `x-init`, and it will be run after:
 
-`x-init="return () => { // we have access to the post-dom-initialization state here // }"`
+`x-init="() => { // we have access to the post-dom-initialization state here // }"`
 
 ---
 
