diff --git a/README.md b/README.md
index ea5652e6..54498f53 100644
--- a/README.md
+++ b/README.md
@@ -9,14 +9,14 @@ Think of it like Tailwind for JavaScript.
 > Note: This tool's syntax is almost entirely borrowed from VueJs. I am forever grateful for the gift it is to the web.
 
 ## Install
-Add the following script at the end of your `<head>` tag.
-```
+Add the following script to the end of your `<head>` tag.
+```html
 <script src="https://cdn.jsdelivr.net/gh/calebporzio/project-x/dist/project-x.min.js" defer></script>
 ```
 
 ## Use
 *Dropdown/Modal*
-```
+```html
 <div x-data="{ open: false }">
     <button x-on:click="open = true">Open Dropdown</button>
 
@@ -31,7 +31,7 @@ Add the following script at the end of your `<head>` tag.
 ```
 
 *Tabs*
-```
+```html
 <div x-data="{ tab: 'foo' }">
     <button x-bind:class="{ 'active': tab === 'foo' }" x-on:click="tab = 'foo'">Foo</button>
     <button x-bind:class="{ 'active': tab === 'bar' }" x-on:click="tab = 'bar'">Bar</button>
