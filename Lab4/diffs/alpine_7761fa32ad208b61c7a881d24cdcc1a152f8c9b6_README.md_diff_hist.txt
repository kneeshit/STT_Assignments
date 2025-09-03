diff --git a/README.md b/README.md
index 7145ec0f..e3d749fb 100644
--- a/README.md
+++ b/README.md
@@ -400,6 +400,12 @@ The `camel` modifier will attach an event listener for the camel case equivalent
 
 > Note: `x-model` is smart enough to detect changes on text inputs, checkboxes, radio buttons, textareas, selects, and multiple selects. It should behave [how Vue would](https://vuejs.org/v2/guide/forms.html) in those scenarios.
 
+**`.number` modifier**
+**Example:** `<input x-model.number="age">`
+
+The `number` modifier will convert the input's value to a number.
+
+
 **`.debounce` modifier**
 **Example:** `<input x-model.debounce="search">`
 
