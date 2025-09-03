diff --git a/README.md b/README.md
index 85908ec9..5df852bb 100644
--- a/README.md
+++ b/README.md
@@ -113,6 +113,7 @@ There are 13 directives available to you:
 | [`x-if`](#x-if) | Remove an element completely from the DOM. Needs to be used on a `<template>` tag. |
 | [`x-for`](#x-for) | Create new DOM nodes for each item in an array. Needs to be used on a `<template>` tag. |
 | [`x-transition`](#x-transition) | Directives for applying classes to various stages of an element's transition |
+| [`x-spread`](#x-spread) | Allows you to bind an object of Alpine directives to an element for better reausibility |
 | [`x-cloak`](#x-cloak) | This attribute is removed when Alpine initializes. Useful for hiding pre-initialized DOM. |
 
 And 6 magic properties:
@@ -525,6 +526,51 @@ These behave exactly like VueJs's transition directives, except they have differ
 
 ---
 
+### `x-spread`
+**Example:**
+```html
+<div x-data="dropdown">
+    <button x-spread="trigger">Open Dropdown</button>
+
+    <span x-spread="dialogue">Dropdown Contents</span>
+</div>
+
+<script>
+    function dropdown() {
+        return {
+            open: false,
+            trigger: {
+                ['@click']() {
+                    this.open = true
+                },
+            },
+            dialogue: {
+                ['x-show']() {
+                    return this.open
+                },
+                ['@click.away']() {
+                    this.open = false
+                },
+            }
+        }
+    }
+</script>
+```
+
+`x-spread` allows you to extract an elements Alpine bindings into a reusable object.
+
+The object keys are the directives (Can be any directive including modifiers), and the values are callbacks to be evaluated by Alpine.
+
+> Note: The only anomoly with x-spread is when used with `x-for`. When the directive being "spread" is `x-for`, you should return a normal expression string from the callback. For example: `['x-for']() { return 'item in items' }`.
+
+```html
+<style>
+    [x-cloak] { display: none; }
+</style>
+```
+
+---
+
 ### `x-cloak`
 **Example:** `<div x-data="{}" x-cloak></div>`
 
