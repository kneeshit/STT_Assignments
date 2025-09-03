diff --git a/inject-version-readme.js b/inject-version-readme.js
index 0cd2c708..86c9df65 100644
--- a/inject-version-readme.js
+++ b/inject-version-readme.js
@@ -5,6 +5,6 @@ const pkg = require('./package.json');
 const readmeTranslations = fs.readdirSync('.').filter((name) => name.includes('README'))
 readmeTranslations.forEach((readmeName) => {
     const original = fs.readFileSync(readmeName, 'utf8')
-    const updated = original.replace(/[0-9]\.[0-9]\.[0-9]/gi, pkg.version)
+    const updated = original.replace(/[0-9]+\.[0-9]+\.[0-9]+/gi, pkg.version)
     fs.writeFileSync(readmeName, updated, 'utf8')
 })
