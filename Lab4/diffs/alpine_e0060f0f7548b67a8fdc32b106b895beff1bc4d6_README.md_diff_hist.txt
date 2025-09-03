diff --git a/README.md b/README.md
index 9958d88c..38228991 100644
--- a/README.md
+++ b/README.md
@@ -74,7 +74,7 @@ Think of it like the `data` property of a Vue component.
 
 **Extract Component Logic**
 
-You can extract data (and behavior) into reausable functions like so:
+You can extract data (and behavior) into reausable functions:
 
 ```html
 <div x-data="dropdown()">
@@ -97,7 +97,7 @@ You can extract data (and behavior) into reausable functions like so:
 </script>
 ```
 
-You can also mix-in multiple data objects with syntax like so:
+You can also mix-in multiple data objects with syntax:
 
 ```html
 <div x-data="{...dropdown(), ...tabs()}">
