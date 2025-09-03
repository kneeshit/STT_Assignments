diff --git a/README.md b/README.md
index da8398ca..98f6ab17 100644
--- a/README.md
+++ b/README.md
@@ -403,7 +403,7 @@ The `camel` modifier will attach an event listener for the camel case equivalent
 **`.number` modifier**
 **Example:** `<input x-model.number="age">`
 
-The `number` modifier will convert the input's value to a number.
+The `number` modifier will convert the input's value to a number. If the value cannot be parsed as a valid number, the original value is returned.
 
 **`.debounce` modifier**
 **Example:** `<input x-model.debounce="search">`
