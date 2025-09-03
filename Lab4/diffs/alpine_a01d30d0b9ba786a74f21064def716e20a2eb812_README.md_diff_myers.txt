diff --git a/README.md b/README.md
index 255b476c..91b49c85 100644
--- a/README.md
+++ b/README.md
@@ -301,6 +301,20 @@ Adding `.window` to an event listener will install the listener on the global wi
 
 Adding the `.once` modifier to an event listener will ensure that the listener will only be handled once. This is useful for things you only want to do once, like fetching HTML partials and such.
 
+**`.debounce` modifier**
+**Example:** `<input x-on:input.debounce="fetchSomething()">`
+
+The `debounce` modifier allows you to "debounce" an event handler. In other words, the event handler will NOT run until a certain amount of time has elapsed since the last event that fired. When the handler is ready to be called, the last handler call will execute.
+
+The default debounce "wait" time is 250 milliseconds.
+
+If you wish to customize this, you can specifiy a custom wait time like so:
+
+```
+<input x-on:input.debounce.750="fetchSomething()">
+<input x-on:input.debounce.750ms="fetchSomething()">
+```
+
 ---
 
 ### `x-model`
@@ -312,6 +326,20 @@ Adding the `.once` modifier to an event listener will ensure that the listener w
 
 > Note: `x-model` is smart enough to detect changes on text inputs, checkboxes, radio buttons, textareas, selects, and multiple selects. It should behave [how Vue would](https://vuejs.org/v2/guide/forms.html) in those scenarios.
 
+**`.debounce` modifier**
+**Example:** `<input x-model.debounce="search">`
+
+The `debounce` modifier allows you to add a "debounce" to a value update. In other words, the event handler will NOT run until a certain amount of time has elapsed since the last event that fired. When the handler is ready to be called, the last handler call will execute.
+
+The default debounce "wait" time is 250 milliseconds.
+
+If you wish to customize this, you can specifiy a custom wait time like so:
+
+```
+<input x-model.debounce.750="search">
+<input x-model.debounce.750ms="search">
+```
+
 ---
 
 ### `x-text`
