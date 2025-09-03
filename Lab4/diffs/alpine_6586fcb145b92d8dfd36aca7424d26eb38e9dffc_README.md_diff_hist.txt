diff --git a/README.md b/README.md
index 2c0b1025..1c9311d0 100644
--- a/README.md
+++ b/README.md
@@ -447,6 +447,8 @@ It's important that `x-if` is used on a `<template></template>` tag because Alpi
 
 > Note: `x-if` must have a single element root inside the `<template></template>` tag.
 
+> Note: When using `template` in a `svg` tag, you need to add a [polyfill](https://github.com/alpinejs/alpine/issues/637#issuecomment-654856538) that should be run before Alpine.js is initialized.
+
 ---
 
 ### `x-for`
@@ -472,6 +474,8 @@ If you want to access the current index of the iteration, use the following synt
 
 > Note: `x-for` must have a single element root inside of the `<template></template>` tag.
 
+> Note: When using `template` in a `svg` tag, you need to add a [polyfill](https://github.com/alpinejs/alpine/issues/637#issuecomment-654856538) that should be run before Alpine.js is initialized.
+
 #### Nesting `x-for`s
 You can nest `x-for` loops, but you MUST wrap each loop in an element. For example:
 
