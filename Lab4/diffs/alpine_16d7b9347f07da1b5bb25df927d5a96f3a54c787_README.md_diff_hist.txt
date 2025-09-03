diff --git a/README.md b/README.md
index 2c0524df..80f21bd7 100644
--- a/README.md
+++ b/README.md
@@ -589,7 +589,7 @@ If you need to access $event inside of a JavaScript function you can pass it in
 </div>
 ```
 
-Notice that, because of [event bubling](https://en.wikipedia.org/wiki/Event_bubbling), you'll need to use the [`.window`](https://github.com/alpinejs/alpine#x-on) modifier if you are trying to propagate events between sibling nodes:
+Notice that, because of [event bubbling](https://en.wikipedia.org/wiki/Event_bubbling), you'll need to use the [`.window`](https://github.com/alpinejs/alpine#x-on) modifier if you are trying to propagate events between sibling nodes:
 
 ```html
 <div @foo-event.window="console.log($event.detail.foo)">
