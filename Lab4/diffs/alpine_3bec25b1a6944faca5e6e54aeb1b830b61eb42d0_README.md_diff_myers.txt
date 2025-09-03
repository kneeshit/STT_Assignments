diff --git a/README.md b/README.md
index 0b8ba323..9958d88c 100644
--- a/README.md
+++ b/README.md
@@ -97,6 +97,12 @@ You can extract data (and behavior) into reausable functions like so:
 </script>
 ```
 
+You can also mix-in multiple data objects with syntax like so:
+
+```html
+<div x-data="{...dropdown(), ...tabs()}">
+```
+
 ---
 
 ### `x-bind`
