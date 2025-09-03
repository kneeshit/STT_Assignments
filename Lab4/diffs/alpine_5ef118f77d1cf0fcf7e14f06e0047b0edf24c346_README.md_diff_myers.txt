diff --git a/README.md b/README.md
index 085e1d72..f0d45309 100644
--- a/README.md
+++ b/README.md
@@ -12,7 +12,7 @@ Think of it like [Tailwind](https://tailwindcss.com/) for JavaScript.
 
 **From CDN:** Add the following script to the end of your `<head>` section.
 ```html
-<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.2.0/dist/alpine.js" defer></script>
+<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.3.0/dist/alpine.js" defer></script>
 ```
 
 That's it. It will initialize itself.
@@ -82,11 +82,12 @@ You can even use it for non-trivial things:
 
 ## Learn
 
-There are 11 directives available to you:
+There are 12 directives available to you:
 
 | Directive
 | --- |
 | [`x-data`](#x-data) |
+| [`x-init`](#x-init) |
 | [`x-show`](#x-show) |
 | [`x-bind`](#x-bind) |
 | [`x-on`](#x-on) |
@@ -145,6 +146,15 @@ You can also mix-in multiple data objects using object destructuring:
 
 ---
 
+### `x-init`
+**Example:** `<div x-data"{ foo: 'bar' }" x-init="foo = 'baz"></div>`
+
+**Structure:** `<div x-data="..." x-init="[expression]"></div>`
+
+`x-init` runs an expression (with the initial data object in scope) when a component is initialized.
+
+---
+
 ### `x-show`
 **Example:** `<div x-show="open"></div>`
 
