diff --git a/README.md b/README.md
index 99e1ab4d..261cc2d2 100644
--- a/README.md
+++ b/README.md
@@ -407,6 +407,19 @@ If you want to access the current index of the iteration, use the following synt
 </template>
 ```
 
+#### Nesting `x-for`s
+You can nest `x-for` loops, but you MUST wrap each loop in an element. For example:
+
+```html
+<template x-for="item in items">
+    <div>
+        <template x-for="subItem in item.subItems">
+            <div x-text="subItem"></div>
+        </template>
+    </div>
+</template>
+```
+
 ---
 
 ### `x-transition`
