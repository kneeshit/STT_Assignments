diff --git a/README.pt.md b/README.pt.md
index db5dd05f..c5e8ad52 100644
--- a/README.pt.md
+++ b/README.pt.md
@@ -6,7 +6,7 @@
 
 O Alpine.js oferece a natureza reativa e declarativa de grandes estruturas, como Vue ou React, a um custo muito menor.
 
-Podemos manter a DOM e abrilhantar o comportamento como acharmos melhor.
+Podemos manter a DOM e aperfeiçoar o comportamento como acharmos melhor.
 
 Pensem nisso como o [Tailwind](https://tailwindcss.com/) para JavaScript.
 
@@ -14,41 +14,41 @@ Pensem nisso como o [Tailwind](https://tailwindcss.com/) para JavaScript.
 
 ## Instalação
 
-**No CDN:** Adicionem o seguinte script ao final da seção `<head>`.
+**Via CDN:** Adicionem o seguinte script no final da seção `<head>`.
 
 ```html
 <script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script>
 ```
 
-E é isso. Ele irá se inicializar.
+E é isso. Ele vai se inicializar.
 
-Para ambiente de produção, é recomendável fixar um número de versão específico no link para evitar problemas inesperadas das versões mais recentes.
+Para ambiente de produção, é recomendado fixar o número da versão específico no link para evitar problemas inesperadas das versões mais recentes.
 Por exemplo, para usar a versão `2.3.5`:
 
 ```html
 <script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.3.5/dist/alpine.min.js" defer></script>
 ```
 
-**No NPM:** Instale o pacote no NPM.
+**Via NPM:** Instale o pacote pelo NPM.
 
 ```js
 npm i alpinejs
 ```
 
-Inclua no script.
+Incluir no script.
 
 ```js
 import 'alpinejs';
 ```
 
-**Para suportar o IE11** Use os seguintes scripts.
+**Para suportar IE11** Usar os seguintes scripts.
 
 ```html
 <script type="module" src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"></script>
 <script nomodule src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine-ie11.min.js" defer></script>
 ```
 
-O padrão acima é o [padrão de módulo/nomodule](https://philipwalton.com/articles/deploying-es2015-code-in-production-today/) que resultará no pacote moderno carregado automaticamente em browsers modernos e o Pacote IE11 carregado automaticamente no IE11 e em outros browsers herdados.
+O padrão acima é o [padrão de módulo/nomodule](https://philipwalton.com/articles/deploying-es2015-code-in-production-today/) que resulta num pacote moderno carregado automaticamente em browsers modernos e o pacote IE11 carregado automaticamente no IE11 e em outros browsers herdados.
 
 ## Usar
 
@@ -81,7 +81,7 @@ _Tabs_
 ```
 
 Podemos até usá-lo para coisas não triviais:
-_Pré pedido de conteudo para HTML dropdown's ao passar com o rato_
+_Pré pedido de conteudo para o HTML da dropdown ao passar com o rato_
 
 ```html
 <div x-data="{ open: false }">
@@ -108,19 +108,19 @@ Existem 14 diretrizes disponíveis:
 
 | Directiva                       | Descrição                                                                                                                     |
 | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
-| [`x-data`](#x-data)             | Declara um novo scope de componente.                                                                                          |
+| [`x-data`](#x-data)             | Declara um novo scope do componente.                                                                                          |
 | [`x-init`](#x-init)             | Executa uma expressão quando um componente é inicializado.                                                                    |
 | [`x-show`](#x-show)             | Alterna `display: none;` no elemento dependendo da expressão (verdadeiro ou falso).                                           |
-| [`x-bind`](#x-bind)             | Define o valor de um atributo para o resultado de uma expressão JS                                                            |
+| [`x-bind`](#x-bind)             | Define o valor de um atributo para o resultado de uma expressão JS.                                                            |
 | [`x-on`](#x-on)                 | Anexa um evento de escuta ao elemento. Executa a expressão JS quando emitida.                                                 |
 | [`x-model`](#x-model)           | Adiciona "ligação de dados bidirecional" a um elemento. Mantém o elemento de entrada sincronizado com os dados do componente. |
 | [`x-text`](#x-text)             | Funciona da mesma forma que o `x-bind`, mas atualiza o `innerText` de um elemento.                                             |
 | [`x-html`](#x-html)             | Funciona de maneira semelhante ao `x-bind`, mas atualiza o `innerHTML` de um elemento.                                         |
 | [`x-ref`](#x-ref)               | Maneira conveniente de recuperar elementos DOM fora do seu componente.                                                        |
-| [`x-if`](#x-if)                 | Remove um elemento completamente do DOM. Precisa ser usado em uma tag `<template>`.                                           |
-| [`x-for`](#x-for)               | Crie novos nós DOM para cada item em uma matriz. Precisa ser usado em uma tag `<template>`.                                   |
-| [`x-transition`](#x-transition) | Diretrizes para aplicar classes a vários estágios da transição de um elemento                                                 |
-| [`x-spread`](#x-spread)         | Permite vincular um objeto de diretivas Alpine a um elemento para melhor reutilização                                         |
+| [`x-if`](#x-if)                 | Remove um elemento completamente na DOM. Precisa de usar uma tag `<template>`.                                           |
+| [`x-for`](#x-for)               | Crie novos nós DOM para cada item em uma matriz. Precisa de usar uma tag `<template>`.                                   |
+| [`x-transition`](#x-transition) | Diretrizes para aplicar classes a vários estágios da transição de um elemento.                                                 |
+| [`x-spread`](#x-spread)         | Permite definir um objeto de diretivas Alpine, a um elemento para melhor reutilização.                                         |
 | [`x-cloak`](#x-cloak)           | Este atributo é removido quando o Alpine é inicializado. Útil para ocultar a pré-inicialização da DOM.                       |
 
 E 6 propriedades mágicas:
@@ -129,16 +129,16 @@ E 6 propriedades mágicas:
 | ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
 | [`$el`](#el)             | Recupere o nó DOM do componente raiz.                                                                            |
 | [`$refs`](#refs)         | Recupera elementos DOM marcados com `x-ref` dentro do componente.                                                |
-| [`$event`](#event)       | Recupera o objeto "Evento" do browser nativo em um evento que esteja a escuta.                                   |
+| [`$event`](#event)       | Recupera o objeto "Evento" do browser nativo em um evento que estejamos a escuta.                                   |
 | [`$dispatch`](#dispatch) | Cria um `CustomEvent` e envio-o usando `.dispatchEvent ()` internamente.                                           |
-| [`$nextTick`](#nexttick) | Execute uma determinada expressão APÓS a Alpine fazer suas atualizações reativas do DOM.                         |
-| [`$watch`](#watch)       | Disparará um retorno de chamada fornecido quando uma propriedade do componente que está a "escuta" for alterada. |
+| [`$nextTick`](#nexttick) | Execute uma determinada expressão APÓS o Alpine fazer suas atualizações reativas na DOM.                         |
+| [`$watch`](#watch)       | Disparará um callback fornecida quando uma propriedade do componente que está a "escuta" for alterada. |
 
 ## Patrocinadores
 
 <img width="33%" src="https://refactoringui.nyc3.cdn.digitaloceanspaces.com/tailwind-logo.svg" alt="Tailwind CSS">
 
-**Queres o teu logotipo aqui? [Mensagem no Twitter](https://twitter.com/calebporzio)**
+**Queres o teu logótipo aqui? [Mensagem pelo Twitter](https://twitter.com/calebporzio)**
 
 ## Colaboradores VIP
 
@@ -163,11 +163,11 @@ E 6 propriedades mágicas:
 
 `x-data` declara um novo scope do componente. Diz à estrutura para inicializar um novo componente com o seguinte objeto de dados.
 
-Pense nisso como a propriedade `data` de um componente Vue.
+Pensem nisso como a propriedade `data` de um componente Vue.
 
-**Extrair Lógica de Componentes**
+**Extrair Lógica dos Componentes**
 
-Podemos extrair dados (e comportamento) em funções reutilizáveis:
+Podemos extrair dados (e comportamentos) em funções reutilizáveis:
 
 ```html
 <div x-data="dropdown()">
@@ -196,7 +196,7 @@ Podemos extrair dados (e comportamento) em funções reutilizáveis:
 </script>
 ```
 
-> **Para utilizadores do bundler**, observem que o Alpine.js assede a funções que estão no scope global (`window`), vamos precisar atribuir explicitamente as suas funções à `window` para usá-las com `x- data`, por exemplo `window.dropdown = function () {}` (isso ocorre com Webpack, Rollup, Parcel etc. `function`'s que defenir serão padronizados para o scope do módulo, e não para `window`).
+> **Para utilizadores do bundler**, observem que o Alpine.js assede a funções que estão no scope global (`window`), vamos necessitar atribuir explicitamente as suas funções à `window` para usá-las com `x- data`, por exemplo `window.dropdown = function () {}` (isso ocorre com Webpack, Rollup, Parcel etc. `function`'s que defenir serão padronizados para o scope do módulo, e não para `window`).
 
 Também podemos misturar vários objetos de dados usando a desestruturação de objetos:
 
@@ -214,7 +214,7 @@ Também podemos misturar vários objetos de dados usando a desestruturação de
 
 `x-init` executa uma expressão quando um componente é inicializado.
 
-Caso desejem executar o código ANTES do Alpine fazer as atualizações iniciais na DOM (algo como um gancho `mounted ()` no VueJS)), podem retornar um callback do `x-init`, e é executado após:
+Caso desejem executar o código ANTES do Alpine fazer as atualizações iniciais na DOM (algo como um gancho `mounted ()` no VueJS), podemos retornar um callback do `x-init`, e é executado após:
 
 `x-init="() => { // temos acesso ao estado de pós-inicialização aqui // }"`
 
@@ -242,15 +242,15 @@ Caso desejem executar o código ANTES do Alpine fazer as atualizações iniciais
 | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
 | `x-show.transition`                                     | Desvanecer e escala em simultâneos. (opacity, scale: 0.95, timing-function: cubic-bezier(0.4, 0.0, 0.2, 1), duration-in: 150ms, duration-out: 75ms) |
 | `x-show.transition.in`                                  | Apenas transição de entrada.                                                                                                                        |
-| `x-show.transition.out`                                 | Apenas transição de saida.                                                                                                                          |
+| `x-show.transition.out`                                 | Apenas transição de saída.                                                                                                                          |
 | `x-show.transition.opacity`                             | Apenas transição de desvanecer.                                                                                                                     |
 | `x-show.transition.scale`                               | Apenas transição de escala.                                                                                                                         |
 | `x-show.transition.scale.75`                            | Personalizar a transformação de escala CSS `transform: scale(.75)`.                                                                                 |
 | `x-show.transition.duration.200ms`                      | Define a transição "entrada" para 200ms. A saída é ajustada para metade disso (100ms).                                                           |
 | `x-show.transition.origin.top.right`                    | Personalizar a origem da transformação CSS `transform-origin: top right`.                                                                           |
-| `x-show.transition.in.duration.200ms.out.duration.50ms` | Durações diferentes para "entrada" e "saida".                                                                                                       |
+| `x-show.transition.in.duration.200ms.out.duration.50ms` | Durações diferentes para "entrada" e "saída".                                                                                                       |
 
-> Nota: Todos esses modificadores de transição podem ser usados em conjunto. Isso é possível (apesar de ridículo: lol): `x-show.transition.in.duration.100ms.origin.top.right.opacity.scale.85.out.duration.200ms.origin.bottom.left.opacity.scale.95`
+> Nota: Todos esses modificadores de transição podem ser usados em conjunto. Isso é possível (apesar de não fazer sentido): `x-show.transition.in.duration.100ms.origin.top.right.opacity.scale.85.out.duration.200ms.origin.bottom.left.opacity.scale.95`
 
 > Nota: `x-show` espera que todas os filhos terminem a transição. Caso desejem ignorar esse comportamento, adicionem o modificador `.immediate`:
 
@@ -264,19 +264,19 @@ Caso desejem executar o código ANTES do Alpine fazer as atualizações iniciais
 
 ### `x-bind`
 
-> Nota: Podem usar a sintaxe ":" mais curta: `:type =" ... "`
+> Nota: Podemos usar uma sintaxe ":" mais curta: `:type =" ... "`
 
 **Exemplo:** `<input x-bind:type="inputType">`
 
 **Estrutura:** `<input x-bind:[attribute]="[expressão]">`
 
-`x-bind` define o valor de um atributo para o resultado de uma expressão JavaScript. A expressão tem acesso a todas as chaves do objeto de dados do componente e é atualizada sempre que seus dados forem atualizados.
+`x-bind` define o valor de um atributo para o resultado de uma expressão JavaScript. A expressão tem acesso a todas as chaves do objeto de dados do componente e é atualizada sempre que os dados forem atualizados.
 
 > Nota: as ligações de atributo APENAS são atualizadas quando as dependências são atualizadas. A estrutura é inteligente o suficiente para observar alterações nos dados e detectar quais ligações se importam com elas.
 
 **`x-bind` para atributos de classes**
 
-`x-bind` comporta-se de maneira um pouco diferente ao vincular o atributo`class`.
+`x-bind` comporta-se de maneira um pouco diferente ao definir o atributo`class`.
 
 Para classes, passamos um objeto cujas as chaves são nomes de classe e valores são expressões booleanas para determinar se esses nomes de classe são aplicados ou não.
 
@@ -308,13 +308,13 @@ Os atributos booleanos são suportados de acordo com a [especificação HTML](ht
 **`.camel` modificador**
 **Exemplo:** `<svg x-bind:view-box.camel="viewBox">`
 
-O modificador `camel` se ligará ao equivalente em maiúsculas e minúsculas do nome do atributo. No exemplo acima, o valor de `viewBox` é vinculado ao atributo`viewBox` em oposição ao atributo `viewbox`.
+O modificador `camel` se ligará ao equivalente em maiúsculas e minúsculas do nome do atributo. No exemplo acima, o valor de `viewBox` é definido ao atributo`viewBox` em oposição ao atributo `viewbox`.
 
 ---
 
 ### `x-on`
 
-> Nota: podem usar a sintaxe "@" mais curta: `@click =" ... "
+> Nota: podemos usar a sintaxe "@" mais curta: `@click =" ... "
 
 **Exemplo:** `<button x-on:click="foo = 'bar'"></button>`
 
@@ -322,9 +322,9 @@ O modificador `camel` se ligará ao equivalente em maiúsculas e minúsculas do
 
 O `x-on` anexa um evento de escuta ao elemento em que está declarado. Quando esse evento é emitido, a expressão JavaScript definida como seu valor é executada.
 
-Caso algum dado for modificado na expressão, outros atributos do elemento "vinculados" a esses dados serão atualizados.
+Caso algum dado for modificado na expressão, outros atributos do elemento "definidos" a esses dados serão atualizados.
 
-> Nota: Também podem especificar um nome de função JavaScript
+> Nota: Também podemos especificar um nome de função JavaScript
 
 **Exemplo:** `<button x-on:click="myFunction"></button>`
 
@@ -338,15 +338,15 @@ Podemos especificar chaves específicas para escutar usando modificadores de key
 
 Exemplos: `enter`, `escape`, `arrow-up`, `arrow-down`
 
-> Nota: Também podem ouvir a combinações de teclas do sistema como: `x-on:keydown.cmd.enter="foo"`
+> Nota: Também podemos ouvir a combinações de teclas do sistema como: `x-on:keydown.cmd.enter="foo"`
 
 **`.away` modificador**
 
 **Exemplo:** `<div x-on:click.away="showModal = false"></div>`
 
-Quando o modificador `.away` estiver presente, o manipulador de eventos é executado apenas quando o evento se originar de uma fonte que não seja ela própria ou seus filhos.
+Quando o modificador `.away` estiver presente, o evento handler é executado apenas quando o evento se originar de uma fonte que não seja ela própria ou seus filhos.
 
-Isso é útil para ocultar dropdowns e modais quando um utilizador clicar longe deles.
+Isso é útil para ocultar dropdowns e modals quando um utilizador clicar longe deles.
 
 **`.prevent` modificador**
 **Exemplo:** `<input type="checkbox" x-on:click.prevent>`
@@ -361,12 +361,12 @@ Adicionar `.stop` a um evento de escuta ira chamar o ` stopPropagation` no event
 **`.self` modificador**
 **Exemplo:** `<div x-on:click.self="foo = 'bar'"><button></button></div>`
 
-Adicionar `.self` a um evento de escuta só vai acionar o manipulador quando o` $ event.target` for o próprio elemento. No exemplo acima, isso significa que o evento "click" que borbulha do botão para a `<div>` externo **não** executa o manipulador.
+Adicionar `.self` a um evento de escuta só vai acionar o handler quando o `$event.target` for o próprio elemento. No exemplo acima, isso significa que o evento "click" que borbulha do botão para a `<div>` externo **não** executa o handler.
 
 **`.window` modificador**
 **Exemplo:** `<div x-on:resize.window="isOpen = window.outerWidth > 768 ? false : open"></div>`
 
-Adicionar `.window` a um evento de escuta instalará a escuta no objeto na window global em vez do nó DOM no qual está declarado. Isso é útil para quando desejamos modificar o estado do componente quando algo muda com a window, como o evento de redimensionamento. Neste exemplo, quando a janela tiver mais de 768 pixels de largura, fechamos a modal / dropdown, caso contrário, manteremos o mesmo estado.
+Adicionar `.window` a um evento de escuta instalará a escutas no objeto na window global em vez do nó DOM no qual está declarado. Isso é útil para quando desejamos modificar o estado do componente quando algo muda com a window, como o evento de redimensionamento. Neste exemplo, quando a janela tiver mais de 768 pixels de largura, fechamos a modal/dropdown, caso contrário, manteremos o mesmo estado.
 
 > Nota: Também podemos usar o modificador `.document` para anexar escutas ao` document` em vez de `window`
 
@@ -383,7 +383,7 @@ Adicionar o modificador `.passive` a um evento de escuta fará com que a escuta
 **`.debounce` modificador**
 **Exemplo:** `<input x-on:input.debounce="fetchSomething()">`
 
-O modificador `debounce` permite fazer "debounce" a um manipulador de eventos. Em outras palavras, o manipulador de eventos NÃO será executado até que tenha decorrido um certo tempo desde o último evento que foi disparado. Quando o manipulador estiver pronto para ser chamado, a última chamada do manipulador será executada.
+O modificador `debounce` permite fazer "debounce" a um evento handler. Em outras palavras, o evento handler NÃO será executado até que tenha decorrido um certo tempo desde o último evento que foi disparado. Quando o handler estiver pronto para ser chamado, a última chamada do handler será executada.
 
 O tempo de espera de debounce padrão é de 250 milissegundos.
 
@@ -414,7 +414,7 @@ O `x-model` adiciona "ligação de dados bidirecional" a um elemento. Em outras
 **`.debounce` modificador**
 **Exemplo:** `<input x-model.debounce="search">`
 
-O modificador `debounce` permite adicionar um "debounce" a uma atualização de valor. Em outras palavras, o manipulador de eventos NÃO é executado até que tenha decorrido um certo tempo desde o último evento que foi disparado. Quando o manipulador estiver pronto para ser chamado, a última chamada do manipulador é executada.
+O modificador `debounce` permite adicionar um "debounce" a uma atualização de valor. Em outras palavras, o evento handler NÃO é executado até que tenha decorrido um certo tempo desde o último evento que foi disparado. Quando o handler estiver pronto para ser chamado, a última chamada do handler é executada.
 
 O tempo de espera de debounce padrão é de 250 milissegundos.
 
@@ -445,7 +445,7 @@ O `x-text` funciona da mesma forma que o` x-bind`, exceto que, em vez de atualiz
 
 O `x-html` funciona de maneira semelhante ao` x-bind`, exceto que, em vez de atualizar o valor de um atributo, ele atualiza o `innerHTML` de um elemento.
 
-> :warning: **Use apenas em conteúdo confiável e nunca em conteúdo fornecido pelo utilizador.** :warning:
+> :warning: **Usar apenas em conteúdo confiável e nunca em conteúdo fornecido pelo utilizador.** :warning:
 >
 > A renderização dinâmica do HTML de terceiros pode levar facilmente às vulnerabilidades de [XSS] (https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).
 ---
@@ -456,11 +456,11 @@ O `x-html` funciona de maneira semelhante ao` x-bind`, exceto que, em vez de atu
 
 **Estrutura:** `<div x-ref="[ref name]"></div><button x-on:click="$refs.[ref name].innerText = 'bar'"></button>`
 
-O `x-ref` fornece uma maneira conveniente de recuperar elementos DOM fora do seu componente. Ao definir um atributo `x-ref` em um elemento, torna-o disponível para todos os manipuladores de eventos dentro de um objeto chamando `$refs`.
+O `x-ref` fornece uma maneira conveniente de recuperar elementos DOM fora do seu componente. Ao definir um atributo `x-ref` em um elemento, torna-o disponível para todos os eventos handlers dentro de um objeto chamando `$refs`.
 
 Esta é uma alternativa útil para definir ID's e usar o `document.querySelector` em todo o lago.
 
-> Nota: também podemos vincular valores dinâmicos no x-ref: `<span: x-ref =" item.id "> </span>` se necessário.
+> Nota: também podemos definir valores dinâmicos no x-ref: `<span: x-ref =" item.id "> </span>` se necessário.
 
 ---
 
@@ -470,9 +470,9 @@ Esta é uma alternativa útil para definir ID's e usar o `document.querySelector
 
 **Estrutura:** `<template x-if="[expressão]"><div>Algum elemento</div></template>`
 
-Nos casos em que `x-show` não é suficiente (`x-show` define um elemento para `display: none` se for falso),`x-if` pode ser usado para remover um elemento completamente do DOM.
+Nos casos em que `x-show` não é suficiente (`x-show` define um elemento para `display: none` se for falso),`x-if` pode ser usado para remover um elemento completamente na DOM.
 
-É importante que o `x-if` seja usado em uma tag `<template> </template>` porque o Alpine não usa um DOM virtual. Essa implementação permite que a Alpine permaneça robusta e use o DOM real para fazer sua mágia.
+É importante que o `x-if` seja usado em uma tag `<template> </template>` porque o Alpine não usa um DOM virtual. Essa implementação permite que o Alpine permaneça robusta e use o DOM real para fazer sua mágia.
 
 > Nota: `x-if` deve ter uma raiz de elemento único dentro da tag` <template> </template> `.
 
@@ -604,9 +604,9 @@ Elas se comportam exatamente como as diretivas de transição do VueJs, exceto q
 
 O `x-spread` permite extrair as ligações de um elemento Alpine em um objeto reutilizável.
 
-As chaves do objeto são as diretivas (pode ser qualquer diretiva, incluindo modificadores), e os valores são chamadas de retorno a serem avaliados pelo Alpine.
+As chaves do objeto são as diretivas (pode ser qualquer diretiva, incluindo modificadores), e os valores são callback's a serem avaliados pelo Alpine.
 
-> Nota: A única anomalia com propagação x é quando usada com `x-for`. Quando a diretiva "spread" é `x-for`, devemos retornar uma string de expressão normal a partir da chamada de retorno. Por exemplo: `['x-for'] () {return 'item in items'}`.
+> Nota: A única anomalia com propagação x é quando usada com `x-for`. Quando a diretiva "spread" é `x-for`, devemos retornar uma string de expressão normal a partir de um callback. Por exemplo: `['x-for'] () {return 'item in items'}`.
 ---
 
 ### `x-cloak`
@@ -650,7 +650,7 @@ Os atributos `x-cloak` são removidos dos elementos quando o Alpine é inicializ
 <button x-on:click="$refs.foo.innerText = 'bar'"></button>
 ```
 
-`$refs` é uma propriedade mágica que pode ser usada para recuperar elementos DOM marcados com `x-ref` dentro do componente. Isso é útil quando precisamos manipular manualmente os elementos do DOM.
+`$refs` é uma propriedade mágica que pode ser usada para recuperar elementos DOM marcados com `x-ref` dentro do componente. Isso é útil quando necessitamos manipular manualmente os elementos na DOM.
 
 ---
 
@@ -666,7 +666,7 @@ Os atributos `x-cloak` são removidos dos elementos quando o Alpine é inicializ
 
 > Nota: A propriedade $event está disponível apenas nas expressões DOM.
 
-Caso precisarem aceder ao $event dentro de uma função JavaScript, podem passá-lo diretamente:
+Caso necessitem aceder ao $event dentro de uma função JavaScript, podemos passa-lo diretamente:
 
 `<button x-on:click="myFunction($event)"></button>`
 
@@ -685,7 +685,7 @@ Caso precisarem aceder ao $event dentro de uma função JavaScript, podem passá
 
 **Nota sobre a propagação de eventos**
 
-Observem que, devido a [evento com bolhas](https://en.wikipedia.org/wiki/Event_bubbling), quando precisam capturar eventos enviados por nós que estão sob a mesma hierarquia de aninhamento, usem o [`.window`](https://github.com/alpinejs/alpine#x-on) modificador:
+Observem que, devido ao [evento com bolhas](https://en.wikipedia.org/wiki/Event_bubbling), quando for preciso capturar eventos enviados pelos nós que estão sob a mesma hierarquia de encadeamento, usem o modificador [`.window`](https://github.com/alpinejs/alpine#x-on):
 
 **Exemplo:**
 
@@ -731,7 +731,7 @@ Também podemos usar `$dispatch()` para acionar atualizações de dados para lig
 
 > Nota: A propriedade $dispatch está disponível apenas nas expressões DOM.
 
-Caso precisarem aceder ao $dispatch dentro de uma função JavaScript, poderão transmiti-la diretamente:
+Caso necessitem aceder ao $dispatch dentro de uma função JavaScript, poderão transmiti-la diretamente:
 
 `<button x-on:click="myFunction($dispatch)"></button>`
 
@@ -770,7 +770,7 @@ Caso precisarem aceder ao $dispatch dentro de uma função JavaScript, poderão
 </div>
 ```
 
-Podemos "assistir" uma propriedade de componente com o método mágico `$watch`. No exemplo acima, quando o botão é clicado e o valor do `open` é alterado, a chamada de retorno fornecida é executada e o novo valor mostrado num `console.log`.
+Podemos "assistir" uma propriedade de componente com o método mágico `$watch`. No exemplo acima, quando o botão é clicado e o valor do `open` é alterado, e o callback fornecida é executada e o novo valor mostrado num `console.log`.
 
 ## Segurança
 
@@ -778,7 +778,7 @@ Caso encontrarem uma vulnerabilidade de segurança, envie um email para [calebpo
 
 O Alpine conta com uma implementação personalizada usando o objeto `Function` para avaliar suas diretivas. Apesar de ser mais seguro que o `eval()`, o seu uso é proibido em alguns ambientes, como o Google Chrome App, usando a Política de Segurança de Conteúdo restritiva (CSP).
 
-Caso usem o Alpine em uma página web que lida com dados confidenciais e exige [CSP](https://csp.withgoogle.com/docs/strict-csp.html), precisam incluir `unsafe-eval` na sua política. Uma política robusta configurada corretamente ajudará a proteger seus utilizadores ao usar dados pessoais ou financeiros.
+Caso usem o Alpine em uma página web que lida com dados confidenciais e exige [CSP](https://csp.withgoogle.com/docs/strict-csp.html), necessitam incluir `unsafe-eval` na sua política. Uma política robusta configurada corretamente ajudará a proteger os utilizadores ao usar dados pessoais ou financeiros.
 
 Como uma política se aplica a todos os scripts da sua página, é importante que outras bibliotecas externas incluídas na página web estejam cuidadosamente revisadas para garantir que sejam confiáveis e não apresentem nenhuma vulnerabilidade de Cross Site Scripting usando a função `eval()` ou manipular o DOM para injetar código malicioso na sua página.
 
