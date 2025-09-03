diff --git a/README.md b/README.md
index 73a0ca52..97baa355 100644
--- a/README.md
+++ b/README.md
@@ -80,7 +80,7 @@ You can extract data (and behavior) into reausable functions:
 <div x-data="dropdown()">
     <button x-on:click="open()">Open</button>
 
-    <div class="hidden" x-bind:class="{ 'hidden': isClosed() }" x-on:click.away="close()">
+    <div x-show="isOpen()" x-on:click.away="close()">
         // Dropdown
     </div>
 </div>
@@ -91,7 +91,7 @@ You can extract data (and behavior) into reausable functions:
             show: false,
             open() { this.show = true },
             close() { this.show = false },
-            isClosed() { return this.show === false },
+            isOpen() { return this.show === true },
         }
     }
 </script>
