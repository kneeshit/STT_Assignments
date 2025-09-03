diff --git a/README.md b/README.md
index bf2aa06d..2e020753 100644
--- a/README.md
+++ b/README.md
@@ -162,6 +162,11 @@ Adding `.prevent` to an event listener will call `preventDefault` on the trigger
 
 Adding `.stop` to an event listener will call `stopPropagation` on the triggered event. In the above example, this means the "click" event won't bubble from the button to the outer `<div>`. Or in other words, when a user clicks the button, `foo` won't be set to `'bar'`.
 
+**`.window` modifier**
+**Example:** `<div x-on:resize.window="isOpen = window.outerWidth > 768 ? false : open"></div>`
+
+Adding `.window` to an event listener will install the listener on the global window object instead of the DOM node on which it is declared. This is useful for when you want to modify component state when something changes with the window, like the resize event. In this example, when the window grows larger than 768 pixels wide, we will close the modal/dropdown, otherwise maintain the same state.
+
 ---
 
 ### `x-model`
