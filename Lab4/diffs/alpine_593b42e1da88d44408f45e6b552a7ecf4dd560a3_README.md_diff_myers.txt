diff --git a/README.md b/README.md
index 5eb4b04b..a53b76a4 100644
--- a/README.md
+++ b/README.md
@@ -102,7 +102,7 @@ There are 13 directives available to you:
 | [`x-transition`](#x-transition) |
 | [`x-cloak`](#x-cloak) |
 
-And 5 magic properties:
+And 6 magic properties:
 
 | Magic Properties
 | --- |
@@ -111,6 +111,7 @@ And 5 magic properties:
 | [`$event`](#event) |
 | [`$dispatch`](#dispatch) |
 | [`$nextTick`](#nexttick) |
+| [`$watch`](#watch) |
 
 
 ### Directives
@@ -500,7 +501,17 @@ You can also use `$dispatch()` to trigger data updates for `x-model` bindings. F
 </div>
 ```
 
-`$nextTick` is a magic property that allows you to only execute a given expression AFTER Alpine has made its reactive DOM updates. This is useful for times you want to interact with the DOM state AFTER it's reflected any data updates you've made.
+---
+
+### `$watch`
+**Example:**
+```html
+<div x-data="{ open: false }" x-init="$watch('open', value => console.log(value))">
+    <button @click="open = ! open">Toggle Open</button>
+</div>
+```
+
+You can "watch" a component property with the `$watch` magic method. In the above example, when the button is clicked and `open` is changed, the provided callback will fire and `console.log` the new value.
 
 ## v3 Roadmap
 * Move from `x-ref` to `ref` for Vue parity
