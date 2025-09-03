diff --git a/README.md b/README.md
index 1cd9c41c..86c048a4 100644
--- a/README.md
+++ b/README.md
@@ -226,6 +226,8 @@ Adding `.stop` to an event listener will call `stopPropagation` on the triggered
 
 Adding `.window` to an event listener will install the listener on the global window object instead of the DOM node on which it is declared. This is useful for when you want to modify component state when something changes with the window, like the resize event. In this example, when the window grows larger than 768 pixels wide, we will close the modal/dropdown, otherwise maintain the same state.
 
+>Note: You can also use the `.document` modifier to attach listeners to `document` instead of `window`
+
 **`.once` modifier**
 **Example:** `<button x-on:mouseenter.once="fetchSomething()"></button>`
 
