diff --git a/README.md b/README.md
index 2520b2ac..e2d98c6a 100644
--- a/README.md
+++ b/README.md
@@ -290,6 +290,11 @@ This will add or remove the `disabled` attribute when `myVar` is true or false r
 
 Boolean attributes are supported as per the [HTML specification](https://html.spec.whatwg.org/multipage/indices.html#attributes-3:boolean-attribute), for example `disabled`, `readonly`, `required`, `checked`, `hidden`, `selected`, `open`, etc.
 
+**`.camel` modifier**
+**Example:** `<svg x-bind:view-box.camel="viewBox">`
+
+The `camel` modifier will bind to the camel case equivalent of the attribute name. In the example above, the value of `viewBox` will be bound the `viewBox` attribute as opposed to the `view-box` attribute.
+
 ---
 
 ### `x-on`
