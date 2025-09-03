diff --git a/README.md b/README.md
index 59e215f6..c3ac9bc8 100644
--- a/README.md
+++ b/README.md
@@ -58,6 +58,7 @@ Structure: `<div x-data="[JSON data object]">...</div>`
 Think of it like the `data` property of a Vue component.
 
 ### x-bind
+---
 Example: `<input x-bind:type="inputType">`
 
 Structure: `<input x-bind:[attribute]="[expression]">`
@@ -78,6 +79,7 @@ For example:
 In this example, the "hidden" class will only be applied when the value of the `foo` data attribute is `true`.
 
 ### `x-on`
+---
 Example: `<button x-on:click="foo = 'bar'"></button>`
 
 Structure: `<button x-on:[event]="[expression]"></button>`
@@ -95,6 +97,7 @@ When the `.away` modifier is present, the event handler will only be executed wh
 This is useful for hiding dropdowns and modals when a user clicks away from them.
 
 ### `x-model`
+---
 Example: `<input type="text" x-model="foo">`
 
 Structure: `<input type="text" x-model="[data item]">`
@@ -104,6 +107,7 @@ Structure: `<input type="text" x-model="[data item]">`
 > Note: `x-model` is smart enough to detect changes on text inputs, checkboxes, radio buttons, textareas, selects, and multiple selects. It should behave [how Vue would](https://vuejs.org/v2/guide/forms.html) in those scenarios.
 
 ### `x-text`
+---
 Example: `<span x-text="foo"></span>`
 
 Structure: `<span x-text="[expression]"`
