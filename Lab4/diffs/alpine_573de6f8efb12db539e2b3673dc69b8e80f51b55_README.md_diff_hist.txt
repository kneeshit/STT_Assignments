diff --git a/README.md b/README.md
index 5f38b08e..bf683839 100644
--- a/README.md
+++ b/README.md
@@ -107,7 +107,7 @@ Think of it like the `data` property of a Vue component.
 
 **Extract Component Logic**
 
-You can extract data (and behavior) into reausable functions:
+You can extract data (and behavior) into reusable functions:
 
 ```html
 <div x-data="dropdown()">
@@ -154,7 +154,7 @@ You can also mix-in multiple data objects using object destructuring:
 
 `x-bind` sets the value of an attribute to the result of a JavaScript expression. The expression has access to all the keys of the component's data object, and will update every-time it's data is updated.
 
-> Note: attribute bindings ONLY update when their dependancies update. The framework is smart enough to observe data changes and detect which bindings care about them.
+> Note: attribute bindings ONLY update when their dependencies update. The framework is smart enough to observe data changes and detect which bindings care about them.
 
 **`x-bind` for class attributes**
 
