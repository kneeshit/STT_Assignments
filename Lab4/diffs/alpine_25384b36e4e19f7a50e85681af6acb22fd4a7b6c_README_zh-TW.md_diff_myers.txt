diff --git a/README_zh-TW.md b/README_zh-TW.md
index b6526dc7..04a29e06 100644
--- a/README_zh-TW.md
+++ b/README_zh-TW.md
@@ -628,7 +628,7 @@ Alpine 依賴使用於 `Function` 物件的自訂實作來求值於其指令。
 
 如果你在處理機敏資料並在要求 [CSP](https://csp.withgoogle.com/docs/strict-csp.html) 的網站上使用 Alpine ，則需要在政策中加入`unsafe-eval` 。正確設定可靠的政策有助於保護使用者在使用個人或財產相關的資料時的安全性。
 
-由於政策適用於網頁中的所有腳本，因此對網站中包含的其他外部程式庫必須要仔細地審查，以保證它們都是值得姓賴的，並且它們不會因為使用 `eval()` 函數或控制 DOM 在頁面中注入惡意程式碼而造成跨網站指令碼的漏洞。
+由於政策適用於網頁中的所有腳本，因此對網站中包含的其他外部程式庫必須要仔細地審查，以保證它們都是值得信賴的，並且它們不會因為使用 `eval()` 函數或控制 DOM 在頁面中注入惡意程式碼而造成跨網站指令碼的漏洞。
  
 ## V3 路線圖
 * Move from `x-ref` to `ref` for Vue parity?
