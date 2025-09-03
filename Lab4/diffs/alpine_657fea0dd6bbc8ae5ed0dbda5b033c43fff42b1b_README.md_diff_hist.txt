diff --git a/README.md b/README.md
index 38228991..3153634c 100644
--- a/README.md
+++ b/README.md
@@ -97,7 +97,7 @@ You can extract data (and behavior) into reausable functions:
 </script>
 ```
 
-You can also mix-in multiple data objects with syntax:
+You can also mix-in multiple data objects using object destructuring:
 
 ```html
 <div x-data="{...dropdown(), ...tabs()}">
