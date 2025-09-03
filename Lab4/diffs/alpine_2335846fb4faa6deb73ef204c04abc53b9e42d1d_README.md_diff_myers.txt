diff --git a/README.md b/README.md
index 4f54d1de..a5627e19 100644
--- a/README.md
+++ b/README.md
@@ -50,13 +50,13 @@ There are 7 directives available to you:
 
 | Directive
 | --- |
-| `x-data` |
-| `x-bind` |
-| `x-on` |
-| `x-model` |
-| `x-text` |
-| `x-ref` |
-| `x-cloak` |
+| [`x-data`](#x-data) |
+| [`x-bind`](#x-bind) |
+| [`x-on`](#x-on) |
+| [`x-model`](#x-model) |
+| [`x-text`](#x-text) |
+| [`x-ref`](#x-ref) |
+| [`x-cloak`](#x-cloak) |
 
 Here's how they each work:
 
@@ -72,6 +72,31 @@ Here's how they each work:
 
 Think of it like the `data` property of a Vue component.
 
+**Extract Component Logic**
+
+You can extract data (and behavior) into reausable functions like so:
+
+```html
+<div x-data="dropdown()">
+    <button x-on:click="open()">Open</button>
+
+    <div class="hidden" x-bind:class="{ 'hidden': isClosed() }" x-on:click.away="close()">
+        // Dropdown
+    </div>
+</div>
+
+<script>
+    function dropdown() {
+        return {
+            show: false,
+            open() { this.show = true },
+            close() { this.show = false },
+            isClosed() { return this.show === false },
+        }
+    }
+</script>
+```
+
 ---
 
 ### `x-bind`
