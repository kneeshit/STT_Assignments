diff --git a/README.md b/README.md
index 57e60156..23b3e6e6 100644
--- a/README.md
+++ b/README.md
@@ -581,6 +581,7 @@ You can "watch" a component property with the `$watch` magic method. In the abov
 * Add `Alpine.directive()`
 * Add `Alpine.component('foo', {...})` (With magic `__init()` method)
 * Dispatch Alpine events for "loaded", "transition-start", etc... (Original PR: #299) ?
+* Remove "object" (and array) syntax from `x-bind:class="{ 'foo': true }"` (PR to add support for object syntax for the `style` attribute: #236)
 
 ## License
 
