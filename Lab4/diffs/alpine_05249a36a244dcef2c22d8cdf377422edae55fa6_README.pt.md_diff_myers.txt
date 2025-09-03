diff --git a/README.pt.md b/README.pt.md
index c5e8ad52..309a5ae7 100644
--- a/README.pt.md
+++ b/README.pt.md
@@ -445,7 +445,7 @@ O `x-text` funciona da mesma forma que o` x-bind`, exceto que, em vez de atualiz
 
 O `x-html` funciona de maneira semelhante ao` x-bind`, exceto que, em vez de atualizar o valor de um atributo, ele atualiza o `innerHTML` de um elemento.
 
-> :warning: **Usar apenas em conteúdo confiável e nunca em conteúdo fornecido pelo utilizador.** :warning:
+> :warning: **Usar apenas em conteúdo de confiança e nunca em conteúdo fornecido pelo utilizador.** :warning:
 >
 > A renderização dinâmica do HTML de terceiros pode levar facilmente às vulnerabilidades de [XSS] (https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).
 ---
@@ -472,7 +472,7 @@ Esta é uma alternativa útil para definir ID's e usar o `document.querySelector
 
 Nos casos em que `x-show` não é suficiente (`x-show` define um elemento para `display: none` se for falso),`x-if` pode ser usado para remover um elemento completamente na DOM.
 
-É importante que o `x-if` seja usado em uma tag `<template> </template>` porque o Alpine não usa um DOM virtual. Essa implementação permite que o Alpine permaneça robusta e use o DOM real para fazer sua mágia.
+É importante que o `x-if` seja usado em uma tag `<template> </template>` porque o Alpine não usa um DOM virtual. Essa implementação permite que o Alpine permaneça robusto e use o DOM real para fazer sua mágia.
 
 > Nota: `x-if` deve ter uma raiz de elemento único dentro da tag` <template> </template> `.
 
