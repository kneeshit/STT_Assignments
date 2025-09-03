diff --git a/README.md b/README.md
index 3153634c..73a0ca52 100644
--- a/README.md
+++ b/README.md
@@ -11,7 +11,7 @@ Think of it like [Tailwind](https://tailwindcss.com/) for JavaScript.
 ## Install
 Add the following script to the end of your `<head>` section.
 ```html
-<script src="https://cdn.jsdelivr.net/gh/calebporzio/project-x@v0.3.0/dist/project-x.min.js" defer></script>
+<script src="https://cdn.jsdelivr.net/gh/calebporzio/project-x@v0.4.0/dist/project-x.min.js" defer></script>
 ```
 
 ## Use
@@ -24,8 +24,7 @@ Add the following script to the end of your `<head>` section.
     <button x-on:click="open = true">Open Dropdown</button>
 
     <ul
-        class="hidden"
-        x-bind:class="{ 'hidden': ! open }"
+        x-show="open"
         x-on:click.away="open = false"
     >
         Dropdown Body
@@ -39,8 +38,8 @@ Add the following script to the end of your `<head>` section.
     <button x-bind:class="{ 'active': tab === 'foo' }" x-on:click="tab = 'foo'">Foo</button>
     <button x-bind:class="{ 'active': tab === 'bar' }" x-on:click="tab = 'bar'">Bar</button>
 
-    <div class="hidden" x-bind:class="{ 'hidden': tab !== 'foo' }">Tab Foo</div>
-    <div class="hidden" x-bind:class="{ 'hidden': tab !== 'bar' }">Tab Bar</div>
+    <div x-show="tab === 'foo'">Tab Foo</div>
+    <div x-show="tab === 'bar'">Tab Bar</div>
 </div>
 ```
 
@@ -51,6 +50,7 @@ There are 7 directives available to you:
 | Directive
 | --- |
 | [`x-data`](#x-data) |
+| [`x-show`](#x-show) |
 | [`x-bind`](#x-bind) |
 | [`x-on`](#x-on) |
 | [`x-model`](#x-model) |
@@ -105,6 +105,15 @@ You can also mix-in multiple data objects using object destructuring:
 
 ---
 
+### `x-show`
+**Example:** `<div x-show="open"></div>`
+
+**Structure:** `<div x-show="[expression]"></div>`
+
+`x-show` toggles the `display: none;` style on the element depending if the expression resolves to `true` or `false`.
+
+---
+
 ### `x-bind`
 **Example:** `<input x-bind:type="inputType">`
 
