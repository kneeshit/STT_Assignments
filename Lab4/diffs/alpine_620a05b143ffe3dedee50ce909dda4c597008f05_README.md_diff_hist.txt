diff --git a/README.md b/README.md
index 401b5a5a..8c01a532 100644
--- a/README.md
+++ b/README.md
@@ -178,10 +178,28 @@ If you wish to run code AFTER Alpine has made its initial updates to the DOM (so
 
 `x-show` toggles the `display: none;` style on the element depending if the expression resolves to `true` or `false`.
 
+**x-show.transition**
+
+`x-show.transition` is a convenience API for making your `x-show`s more pleasant using CSS transitions.
+
+| Directive | Description |
+| --- | --- |
+| `x-show.transition` | A simultanious fade and scale. |
+| `x-show.transition.in` | Ony transition in. |
+| `x-show.transition.out` | Ony transition out. |
+| `x-show.transition.opacity` | Only use the fade. |
+| `x-show.transition.scale` | Only use the scale. |
+| `x-show.transition.scale.75` | Customize the CSS scale transform `transform: scale(.75)`. |
+| `x-show.transition.duration.200ms` | Sets the "in" transition to 200ms. The out will be set to half that (100ms). |
+| `x-show.transition.origin.top.right` | Customize the CSS transform origin `transform-origin: top right`. |
+| `x-show.transition.in.duration.200ms.out.duration.50ms` | Different durations for "in" and "out". |
+
+> Note: All of these transition modifiers can be used in conjunction with each other. This is possible (although rediculous lol): `x-show.transition.in.duration.100ms.origin.top.right.opacity.scale.85.out.duration.200ms.origin.bottom.left.opacity.scale.95`
+
 > Note: `x-show` will wait for any children to finish transitioning out. If you want to bypass this behavior, add the `.immediate` modifer:
 ```html
 <div x-show.immediate="open">
-    <div x-show="open" x-transition:leave="transition-out">
+    <div x-show.transition="open">
 </div>
 ```
 ---
