diff --git a/README.md b/README.md
index c26b7e49..5eb4b04b 100644
--- a/README.md
+++ b/README.md
@@ -133,9 +133,9 @@ You can extract data (and behavior) into reusable functions:
 
 ```html
 <div x-data="dropdown()">
-    <button x-on:click="open()">Open</button>
+    <button x-on:click="open">Open</button>
 
-    <div x-show="isOpen()" x-on:click.away="close()">
+    <div x-show="isOpen()" x-on:click.away="close">
         // Dropdown
     </div>
 </div>
@@ -340,6 +340,8 @@ Adding the `.once` modifier to an event listener will ensure that the listener w
 
 This is a helpful alternative to setting ids and using `document.querySelector` all over the place.
 
+> Note: you can also bind dynamic values for x-ref: `<span :x-ref="item.id"></span>` if you need to.
+
 ---
 
 ### `x-if`
@@ -500,6 +502,9 @@ You can also use `$dispatch()` to trigger data updates for `x-model` bindings. F
 
 `$nextTick` is a magic property that allows you to only execute a given expression AFTER Alpine has made its reactive DOM updates. This is useful for times you want to interact with the DOM state AFTER it's reflected any data updates you've made.
 
+## v3 Roadmap
+* Move from `x-ref` to `ref` for Vue parity
+
 ## License
 
 Copyright © 2019-2020 Caleb Porzio and contributors
