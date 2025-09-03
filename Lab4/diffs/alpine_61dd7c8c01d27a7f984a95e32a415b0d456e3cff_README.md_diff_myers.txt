diff --git a/README.md b/README.md
index 255b476c..bc826382 100644
--- a/README.md
+++ b/README.md
@@ -86,32 +86,32 @@ You can even use it for non-trivial things:
 
 There are 13 directives available to you:
 
-| Directive
-| --- |
-| [`x-data`](#x-data) |
-| [`x-init`](#x-init) |
-| [`x-show`](#x-show) |
-| [`x-bind`](#x-bind) |
-| [`x-on`](#x-on) |
-| [`x-model`](#x-model) |
-| [`x-text`](#x-text) |
-| [`x-html`](#x-html) |
-| [`x-ref`](#x-ref) |
-| [`x-if`](#x-if) |
-| [`x-for`](#x-for) |
-| [`x-transition`](#x-transition) |
-| [`x-cloak`](#x-cloak) |
+| Directive | Description |
+| --- | --- |
+| [`x-data`](#x-data) | Declares a new component scope. |
+| [`x-init`](#x-init) | Runs an expression when a component is initialized. |
+| [`x-show`](#x-show) | Toggles `display: none;` on the element depending on expression (true or false). |
+| [`x-bind`](#x-bind) | Sets the value of an attribute to the result of a JS expression |
+| [`x-on`](#x-on) | Attaches an event listener to the element. Executes JS expression when emitted. |
+| [`x-model`](#x-model) | Adds "two-way data binding" to an element. Keeps input element in sync with component data. |
+| [`x-text`](#x-text) | Works similarly to `x-bind`, but will update the `innerText` of an element. |
+| [`x-html`](#x-html) | Works similarly to `x-bind`, but will update the `innerHTML` of an element. |
+| [`x-ref`](#x-ref) | Convenient way to retrieve raw DOM elements out of your component. |
+| [`x-if`](#x-if) | Remove an element completely from the DOM. Needs to be used on a `<template>` tag. |
+| [`x-for`](#x-for) | Create new DOM nodes for each item in an array. Needs to be used on a `<template>` tag. |
+| [`x-transition`](#x-transition) | Directives for applying classes to various stages of an element's transition |
+| [`x-cloak`](#x-cloak) | This attribute is removed when Alpine initializes. Useful for hiding pre-initialized DOM. |
 
 And 6 magic properties:
 
-| Magic Properties
-| --- |
-| [`$el`](#el) |
-| [`$refs`](#refs) |
-| [`$event`](#event) |
-| [`$dispatch`](#dispatch) |
-| [`$nextTick`](#nexttick) |
-| [`$watch`](#watch) |
+| Magic Properties | Description |
+| --- | --- |
+| [`$el`](#el) |  Retrieve the root component DOM node. |
+| [`$refs`](#refs) | Retrieve DOM elements marked with `x-ref` inside the component. |
+| [`$event`](#event) | Retrieve the native browser "Event" object within an event listener.  |
+| [`$dispatch`](#dispatch) | Create a `CustomEvent` and dispatch it using `.dispatchEvent()` internally. |
+| [`$nextTick`](#nexttick) | Execute a given expression AFTER Alpine has made its reactive DOM updates. |
+| [`$watch`](#watch) | Will fire a provided callback when a component property you "watched" gets changed. |
 
 
 ### Directives
