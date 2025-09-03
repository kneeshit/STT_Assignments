diff --git a/reqwest/examples/wasm_github_fetch/README.md b/reqwest/examples/wasm_github_fetch/README.md
new file mode 100644
index 0000000..9a00393
--- /dev/null
+++ b/reqwest/examples/wasm_github_fetch/README.md
@@ -0,0 +1,15 @@
+## Example usage of Reqwest from WASM
+
+Install wasm-pack with
+
+    npm install
+
+Then you can build the example locally with:
+
+
+    npm run serve
+
+and then visiting http://localhost:8080 in a browser should run the example!
+
+
+This example is loosely based off of [this example](https://github.com/rustwasm/wasm-bindgen/blob/master/examples/fetch/src/lib.rs), an example usage of `fetch` from `wasm-bindgen`.
\ No newline at end of file
