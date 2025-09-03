diff --git a/README.md b/README.md
index 309aaddf..80b99f4e 100644
--- a/README.md
+++ b/README.md
@@ -14,7 +14,7 @@ Think of it like [Tailwind](https://tailwindcss.com/) for JavaScript.
 
 **From CDN:** Add the following script to the end of your `<head>` section.
 ```html
-<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.6.2/dist/alpine.js" defer></script>
+<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.7.0/dist/alpine.js" defer></script>
 ```
 
 That's it. It will initialize itself.
@@ -84,14 +84,12 @@ You can even use it for non-trivial things:
 
 ## Learn
 
-There are 14 directives available to you:
+There are 12 directives available to you:
 
 | Directive
 | --- |
 | [`x-data`](#x-data) |
 | [`x-init`](#x-init) |
-| [`x-created`](#x-created) |
-| [`x-mounted`](#x-mounted) |
 | [`x-show`](#x-show) |
 | [`x-bind`](#x-bind) |
 | [`x-on`](#x-on) |
@@ -158,8 +156,6 @@ You can also mix-in multiple data objects using object destructuring:
 
 ---
 
-> Warning: `x-init` is depricated, in favor of using `x-created` or `x-mounted`. It will be removed in 2.0
-
 ### `x-init`
 **Example:** `<div x-data"{ foo: 'bar' }" x-init="foo = 'baz"></div>`
 
@@ -167,23 +163,9 @@ You can also mix-in multiple data objects using object destructuring:
 
 `x-init` runs an expression when a component is initialized.
 
----
-
-### `x-created`
-**Example:** `<div x-data="{ foo: 'bar' }" x-created="foo = 'baz"></div>`
-
-**Structure:** `<div x-data="..." x-created="[expression]"></div>`
-
-`x-created` runs an expression when a component is initialized, but BEFORE the component initializes the DOM.
-
----
-
-### `x-mounted`
-**Example:** `<div x-data="{ foo: 'bar' }" x-mounted="foo = 'baz"></div>`
-
-**Structure:** `<div x-data="..." x-mounted="[expression]"></div>`
+If you wish to run code AFTER Alpine has made it's initial updates to the DOM (something like a `mounted()` hook in VueJS), you can return a callback from `x-init`, and it will be run after:
 
-`x-mounted` runs an expression when a component is initialized, and AFTER the component initializes the DOM.
+`x-init="return () => { // we have access to the post-dom-initialization state here // }"`
 
 ---
 
