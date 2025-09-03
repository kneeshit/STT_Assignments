diff --git a/README.md b/README.md
index bb87f9fb..7666888e 100644
--- a/README.md
+++ b/README.md
@@ -14,7 +14,7 @@ Think of it like [Tailwind](https://tailwindcss.com/) for JavaScript.
 
 **From CDN:** Add the following script to the end of your `<head>` section.
 ```html
-<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.8.1/dist/alpine.js" defer></script>
+<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v1.8.2/dist/alpine.js" defer></script>
 ```
 
 That's it. It will initialize itself.
@@ -234,6 +234,8 @@ You can specify specific keys to listen for using keydown modifiers appended to
 
 Examples: `enter`, `escape`, `arrow-up`, `arrow-down`
 
+> Note: You can also listen for system-modifier key combinations like: `x-on:keydown.cmd.enter="foo"`
+
 **`.away` modifier**
 
 **Example:** `<div x-on:click.away="showModal = false"></div>`
