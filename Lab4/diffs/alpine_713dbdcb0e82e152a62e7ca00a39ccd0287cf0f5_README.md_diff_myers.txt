diff --git a/README.md b/README.md
index 54498f53..00a302bd 100644
--- a/README.md
+++ b/README.md
@@ -57,9 +57,11 @@ Here's how they each work:
 
 ### `x-data`
 ---
-Example: `<div x-data="{ foo: 'bar' }">...</div>`
 
-Structure: `<div x-data="[JSON data object]">...</div>`
+| | |
+--- | ---
+Example | `<div x-data="{ foo: 'bar' }">...</div>`
+Structure | `<div x-data="[JSON data object]">...</div>`
 
 `x-data` declares a new component scope. It tells the framework to initialize a new component with the following data object.
 
