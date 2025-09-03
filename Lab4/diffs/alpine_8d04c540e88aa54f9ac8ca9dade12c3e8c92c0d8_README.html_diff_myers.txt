diff --git a/README.html b/README.html
index 6495f7c8..a14ddb07 100644
--- a/README.html
+++ b/README.html
@@ -132,6 +132,9 @@
 <td><a href="#refs"><code>$refs</code></a></td>
 </tr>
 <tr>
+<td><a href="#dispatch"><code>$dispatch</code></a></td>
+</tr>
+<tr>
 <td><a href="#nexttick"><code>$nextTick</code></a></td>
 </tr>
 </tbody>
@@ -366,6 +369,24 @@
 </code></pre>
 <p><code>$refs</code> is a magic property that can be used to retrieve DOM elements marked with <code>x-ref</code> inside the component. This is useful when you need to manually manipulate DOM elements.</p>
 <hr>
+<h3 id="-dispatch"><code>$dispatch</code></h3>
+<p><strong>Example:</strong></p>
+<pre><code class="lang-html">&lt;div @custom-event=&quot;console.log($event.detail.foo)&quot;&gt;
+    &lt;button @click=&quot;$dispatch(&#39;custom-event&#39;, { foo: &#39;bar&#39; })&quot;&gt;
+    &lt;!-- When clicked, will console.log &quot;bar&quot; --&gt;
+&lt;/div&gt;
+</code></pre>
+<p><code>$dispatch</code> is a shortcut for creating a <code>CustomEvent</code> and dispatching it using <code>.dispatchEvent()</code> internally. There are lots of good use cases for passing data around and between components using custom events. <a href="https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Creating_and_triggering_events">Read here</a> for more information on the underlying <code>CustomEvent</code> system in browsers.</p>
+<p>You will notice that any data passed as the second parameter to <code>$dispatch(&#39;some-event&#39;, { some: &#39;data&#39; })</code>, becomes available through the new events &quot;detail&quot; property: <code>$event.detail.some</code>. Attaching custom event data to the <code>.detail</code> property is standard practice for <code>CustomEvent</code>s in browsers. <a href="https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent/detail">Read here</a> for more info.</p>
+<p>You can also use <code>$dispatch()</code> to trigger data updates for <code>x-model</code> bindings. For example:</p>
+<pre><code class="lang-html">&lt;div x-data=&quot;{ foo: &#39;bar&#39; }&quot;&gt;
+    &lt;span x-model=&quot;foo&quot;&gt;
+        &lt;button @click=&quot;$dispatch(&#39;input&#39;, &#39;baz&#39;)&quot;&gt;
+        &lt;!-- After the button is clicked, `x-model` will catch the bubbling &quot;input&quot; event, and update foo to &quot;baz&quot;. --&gt;
+    &lt;/span&gt;
+&lt;/div&gt;
+</code></pre>
+<hr>
 <h3 id="-nexttick"><code>$nextTick</code></h3>
 <p><strong>Example:</strong></p>
 <pre><code class="lang-html">&lt;div x-data=&quot;{ fruit: &#39;apple&#39; }&quot;&gt;
