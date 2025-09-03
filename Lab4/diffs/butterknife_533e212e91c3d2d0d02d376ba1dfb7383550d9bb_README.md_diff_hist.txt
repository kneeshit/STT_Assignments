diff --git a/README.md b/README.md
index cb56dd0..d6014c2 100644
--- a/README.md
+++ b/README.md
@@ -70,6 +70,10 @@ dependencies {
 }
 ```
 
+Note: If you are using the new Jack compiler with version 2.2.0 or newer you do not need the
+'android-apt' plugin and can instead replace `apt` with `annotationProcessor` when declaring the
+compiler dependency.
+
 Snapshots of the development version are available in [Sonatype's `snapshots` repository][snap].
 
 
