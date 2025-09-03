diff --git a/README.md b/README.md
index e957e15c..0536fb99 100644
--- a/README.md
+++ b/README.md
@@ -12,7 +12,7 @@ Think of it like [Tailwind](https://tailwindcss.com/) for JavaScript.
 
 **From CDN:** Add the following script to the end of your `<head>` section.
 ```html
-<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.1.5/dist/alpine.js" defer></script>
+<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.2.0/dist/alpine.js" defer></script>
 ```
 
 That's it. It will initialize itself.
@@ -92,6 +92,7 @@ There are 10 directives available to you:
 | [`x-on`](#x-on) |
 | [`x-model`](#x-model) |
 | [`x-text`](#x-text) |
+| [`x-html`](#x-html) |
 | [`x-ref`](#x-ref) |
 | [`x-if`](#x-if) |
 | [`x-transition`](#x-transition) |
@@ -256,6 +257,15 @@ Adding the `.once` modifer to an event listener will ensure that the listener wi
 
 ---
 
+### `x-html`
+**Example:** `<span x-html="foo"></span>`
+
+**Structure:** `<span x-html="[expression]"`
+
+`x-html` works similarly to `x-bind`, except instead of updating the value of an attribute, it will update the `innerHTML` of an element.
+
+---
+
 ### `x-ref`
 **Example:** `<div x-ref="foo"></div><button x-on:click="$refs.foo.innerText = 'bar'"></button>`
 
