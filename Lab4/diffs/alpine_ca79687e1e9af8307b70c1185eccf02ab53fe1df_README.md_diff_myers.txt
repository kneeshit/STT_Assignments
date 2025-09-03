diff --git a/README.md b/README.md
index dffbf5ab..59a65c48 100644
--- a/README.md
+++ b/README.md
@@ -504,6 +504,8 @@ These behave exactly like VueJs's transition directives, except they have differ
 
 ### Magic Properties
 
+> With the exception of `$el`, magic properties are **not available within `x-data`** as the component isn't initialized yet.
+
 ---
 
 ### `$el`
