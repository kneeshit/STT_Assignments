diff --git a/README.md b/README.md
index ed2e145d..41061040 100644
--- a/README.md
+++ b/README.md
@@ -55,12 +55,12 @@ There are 5 directives available to you:
 
 Here's how they each work:
 
+---
+
 ### `x-data`
 
-| | |
---- | ---
-Example | `<div x-data="{ foo: 'bar' }">...</div>`
-Structure | `<div x-data="[JSON data object]">...</div>`
+**Example:** `<div x-data="{ foo: 'bar' }">...</div>`
+**Structure:** `<div x-data="[JSON data object]">...</div>`
 
 `x-data` declares a new component scope. It tells the framework to initialize a new component with the following data object.
 
