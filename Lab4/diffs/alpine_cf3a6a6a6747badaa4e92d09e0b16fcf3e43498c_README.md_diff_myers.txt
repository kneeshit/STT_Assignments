diff --git a/README.md b/README.md
index 4e270a6b..4225a929 100644
--- a/README.md
+++ b/README.md
@@ -108,6 +108,7 @@ And 4 magic properties:
 | --- |
 | [`$el`](#el) |
 | [`$refs`](#refs) |
+| [`$event`](#event) |
 | [`$dispatch`](#dispatch) |
 | [`$nextTick`](#nexttick) |
 
@@ -416,6 +418,16 @@ These behave exactly like VueJs's transition directives, except they have differ
 
 ---
 
+### `$event`
+**Example:**
+```html
+<input x-on:input="alert($event.target.value)">
+```
+
+`$event` is a magic property that can be used within an event listener to retrieve the native browser "Event" object.
+
+---
+
 ### `$dispatch`
 **Example:**
 ```html
