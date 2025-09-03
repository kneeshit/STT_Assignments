diff --git a/README.md b/README.md
index 292aca18..cff876df 100644
--- a/README.md
+++ b/README.md
@@ -355,6 +355,11 @@ Adding `.window` to an event listener will install the listener on the global wi
 
 Adding the `.once` modifier to an event listener will ensure that the listener will only be handled once. This is useful for things you only want to do once, like fetching HTML partials and such.
 
+**`.passive` modifier**
+**Example:** `<button x-on:touchstart.passive="interactive = true"></button>`
+
+Adding the `.passive` modifier to an event listener will make the listener a passive one, which means `preventDefault()` will not work on any events being processed, this can help, for example with scroll performance on touch devices.
+
 **`.debounce` modifier**
 **Example:** `<input x-on:input.debounce="fetchSomething()">`
 
