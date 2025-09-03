diff --git a/README.md b/README.md
index 07eb50ba..b8b6c7ee 100644
--- a/README.md
+++ b/README.md
@@ -506,6 +506,18 @@ You can nest `x-for` loops, but you MUST wrap each loop in an element. For examp
 </template>
 ```
 
+#### Iterating over a range
+
+Alpine supports the `i in n` syntax, where `n` is an integer, allowing you to iterate over a fixed range of elements.
+
+```html
+<template x-for="i in 10">
+    <span x-text="i"></span>
+</template>
+```
+
+This will output 10 spans, starting with an `i` value of 0.
+
 ---
 
 ### `x-transition`
