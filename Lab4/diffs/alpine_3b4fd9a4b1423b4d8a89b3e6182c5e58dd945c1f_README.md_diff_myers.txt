diff --git a/README.md b/README.md
index 50c19251..a6653ac6 100644
--- a/README.md
+++ b/README.md
@@ -14,7 +14,7 @@ Think of it like [Tailwind](https://tailwindcss.com/) for JavaScript.
 
 **From CDN:** Add the following script to the end of your `<head>` section.
 ```html
-<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.6.1/dist/alpine.js" defer></script>
+<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.6.2/dist/alpine.js" defer></script>
 ```
 
 That's it. It will initialize itself.
@@ -84,11 +84,12 @@ You can even use it for non-trivial things:
 
 ## Learn
 
-There are 13 directives available to you:
+There are 14 directives available to you:
 
 | Directive
 | --- |
 | [`x-data`](#x-data) |
+| [`x-init`](#x-init) |
 | [`x-created`](#x-created) |
 | [`x-mounted`](#x-mounted) |
 | [`x-show`](#x-show) |
@@ -126,7 +127,7 @@ Think of it like the `data` property of a Vue component.
 
 **Extract Component Logic**
 
-You can extract data (and behavior) into reusable functions:
+You can extract data (and behavior) into reusable s:
 
 ```html
 <div x-data="dropdown()">
@@ -157,6 +158,17 @@ You can also mix-in multiple data objects using object destructuring:
 
 ---
 
+> Warning: `x-init` is depricated, in favor of using `x-created` or `x-mounted`. It will be removed in 2.0
+
+### `x-init`
+**Example:** `<div x-data"{ foo: 'bar' }" x-init="foo = 'baz"></div>`
+
+**Structure:** `<div x-data="..." x-init="[expression]"></div>`
+
+`x-init` runs an expression when a component is initialized.
+
+---
+
 ### `x-created`
 **Example:** `<div x-data"{ foo: 'bar' }" x-created="foo = 'baz"></div>`
 
