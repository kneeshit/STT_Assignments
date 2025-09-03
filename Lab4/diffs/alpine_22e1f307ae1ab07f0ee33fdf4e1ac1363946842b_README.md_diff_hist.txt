diff --git a/README.md b/README.md
index 5bf879a7..8fd62e39 100644
--- a/README.md
+++ b/README.md
@@ -41,11 +41,11 @@ For IE11, polyfills will need to be provided. Please load the following scripts
 *Dropdown/Modal*
 ```html
 <div x-data="{ open: false }">
-    <button x-on:click="open = true">Open Dropdown</button>
+    <button @click="open = true">Open Dropdown</button>
 
     <ul
         x-show="open"
-        x-on:click.away="open = false"
+        @click.away="open = false"
     >
         Dropdown Body
     </ul>
@@ -55,8 +55,8 @@ For IE11, polyfills will need to be provided. Please load the following scripts
 *Tabs*
 ```html
 <div x-data="{ tab: 'foo' }">
-    <button x-bind:class="{ 'active': tab === 'foo' }" x-on:click="tab = 'foo'">Foo</button>
-    <button x-bind:class="{ 'active': tab === 'bar' }" x-on:click="tab = 'bar'">Bar</button>
+    <button :class="{ 'active': tab === 'foo' }" @click="tab = 'foo'">Foo</button>
+    <button :class="{ 'active': tab === 'bar' }" @click="tab = 'bar'">Bar</button>
 
     <div x-show="tab === 'foo'">Tab Foo</div>
     <div x-show="tab === 'bar'">Tab Bar</div>
@@ -68,15 +68,15 @@ You can even use it for non-trivial things:
 ```html
 <div x-data="{ open: false }">
     <button
-        x-on:mouseenter.once="
+        @mouseenter.once="
             fetch('/dropdown-partial.html')
                 .then(response => response.text())
                 .then(html => { $refs.dropdown.innerHTML = html })
         "
-        x-on:click="open = true"
+        @click="open = true"
     >Show Dropdown</button>
 
-    <div x-ref="dropdown" x-show="open" x-on:click.away="open = false">
+    <div x-ref="dropdown" x-show="open" @click.away="open = false">
         Loading Spinner...
     </div>
 </div>
@@ -174,6 +174,7 @@ You can also mix-in multiple data objects using object destructuring:
 ---
 
 ### `x-bind`
+> Note: You are free to use the shorter ":" syntax: `:type="..."`
 **Example:** `<input x-bind:type="inputType">`
 
 **Structure:** `<input x-bind:[attribute]="[expression]">`
@@ -207,7 +208,7 @@ Most common boolean attributes are supported, like `readonly`, `required`, etc.
 ---
 
 ### `x-on`
-
+> Note: You are free to use the shorter "@" syntax: `@click="..."`
 **Example:** `<button x-on:click="foo = 'bar'"></button>`
 
 **Structure:** `<button x-on:[event]="[expression]"></button>`
