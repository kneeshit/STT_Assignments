diff --git a/README.md b/README.md
index f1246e6..b18cb7f 100644
--- a/README.md
+++ b/README.md
@@ -186,21 +186,6 @@ Download [the latest JAR][2] or grab via Maven:
 
 
 
-ProGuard
---------
-
-Butter Knife generates and uses classes dynamically which means that static
-analysis tools like ProGuard may think they are unused. In order to prevent them
-from being removed explicitly mark them to be kept.
-
-```
--keepclassmembers class **$$ViewInjector {
-  public static void inject(...);
-}
-```
-
-
-
 License
 -------
 
