diff --git a/README.ru.md b/README.ru.md
index 060b8818..0ea06a48 100644
--- a/README.ru.md
+++ b/README.ru.md
@@ -37,13 +37,13 @@ npm i alpinejs
 import 'alpinejs'
 ```
 
-**Для поддержки IE11** Используйте вместо указанных выше следующие скрипты:
+**Для поддержки IE11** используйте вместо указанных выше следующие скрипты:
 ```html
 <script type="module" src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"></script>
 <script nomodule src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine-ie11.min.js" defer></script>
 ```
 
-Паттерн, используемый выше, называется [паттерн module/nomodule](https://philipwalton.com/articles/deploying-es2015-code-in-production-today/). Он позволяет автоматически загружать современный бандл в современных браузерах, а в IE11 и других устаревших браузерах – бандл для IE11.
+Паттерн, использующийся выше, называется [паттерн module/nomodule](https://philipwalton.com/articles/deploying-es2015-code-in-production-today/). Он позволяет автоматически загружать современный бандл в современных браузерах, а в IE11 и других устаревших браузерах – бандл для IE11.
 
 ## Использование
 
