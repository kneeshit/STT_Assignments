diff --git a/README.md b/README.md
index 5d2d61a5..c473edab 100644
--- a/README.md
+++ b/README.md
@@ -217,7 +217,7 @@ If you wish to run code AFTER Alpine has made its initial updates to the DOM (so
 | `x-show.transition.origin.top.right` | Customize the CSS transform origin `transform-origin: top right`. |
 | `x-show.transition.in.duration.200ms.out.duration.50ms` | Different durations for "in" and "out". |
 
-> Note: All of these transition modifiers can be used in conjunction with each other. This is possible (although rediculous lol): `x-show.transition.in.duration.100ms.origin.top.right.opacity.scale.85.out.duration.200ms.origin.bottom.left.opacity.scale.95`
+> Note: All of these transition modifiers can be used in conjunction with each other. This is possible (although ridiculous lol): `x-show.transition.in.duration.100ms.origin.top.right.opacity.scale.85.out.duration.200ms.origin.bottom.left.opacity.scale.95`
 
 > Note: `x-show` will wait for any children to finish transitioning out. If you want to bypass this behavior, add the `.immediate` modifer:
 ```html
@@ -243,7 +243,7 @@ If you wish to run code AFTER Alpine has made its initial updates to the DOM (so
 
 `x-bind` behaves a little differently when binding to the `class` attribute.
 
-For classes, you pass in an object who's keys are class names, and values are boolean expressions to determine if those class names are applied or not.
+For classes, you pass in an object whose keys are class names, and values are boolean expressions to determine if those class names are applied or not.
 
 For example:
 `<div x-bind:class="{ 'hidden': foo }"></div>`
