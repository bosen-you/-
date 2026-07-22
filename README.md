# 情緒手搖釀造廠｜Emotion Bubble Tea Brewery

一個 30 秒完成的療癒系點擊小遊戲：選基底 → 加情緒配料 → 瘋狂攪拌，最後生成專屬的「情緒特調卡片」，並附上門市兌換流程。

## 內容微調

所有文案與資料都集中在 `index.html` 的 `<script>` 區塊：

- `BASES`：三種基底（氣泡水 / 濃茶 / 岩漿），可調整名稱、描述、顏色 class。
- `TOPPINGS`：五種情緒配料，可增減或改名稱、對應情緒、飲料配料名稱。
- `EMOTION_QUOTES` / `GENERAL_QUOTES`：結果頁的暖心語錄，可自由替換成品牌調性的文字。
