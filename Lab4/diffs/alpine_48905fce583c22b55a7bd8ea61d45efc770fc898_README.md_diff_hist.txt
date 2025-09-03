diff --git a/README.md b/README.md
index 476e422f..adcbb115 100644
--- a/README.md
+++ b/README.md
@@ -407,6 +407,8 @@ If you want to access the current index of the iteration, use the following synt
 </template>
 ```
 
+> Note: `x-for` must have a single element root inside of the `<template></template>` tag.
+
 #### Nesting `x-for`s
 You can nest `x-for` loops, but you MUST wrap each loop in an element. For example:
 
