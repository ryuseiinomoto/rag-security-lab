# 会社フォルダの設計

2026-10-28 · M2

## フォルダ構成

```
data/<会社名>/
├── faq.json
├── terms.md
├── inquiries.json
├── customers.csv
└── orders.json
```

コードは会社フォルダの中身を知らない。フォルダを差し替えれば別の会社で動く（N-02）。

## ファイルごとの形式と項目

| ファイル | 形式 | 項目 | 理由 |
| --- | --- | --- | --- |
| faq.json | JSON | faq_id, category, question, answer | 回答は改行を含む長文になるので |
| terms.md | Markdown | 見出し（章）＋本文 | 人が読む文章。見出しがチャンク分割の単位になる |
| inquiries.json | JSON | inquiry_id, customer_id, date, question, reply | 顧客の文に改行やURLが入る。R-3の攻撃文もここに仕込む |
| customers.csv | CSV | customer_id, name, birth_date, address | 1行1件の表。入れ子なし。住所と生年月日がR-1で「漏れる情報」 |
| orders.json | JSON | order_id, customer_id, order_date, status, items: [{product, category, price, quantity}] | 1注文に商品が複数（入れ子）。statusと日付は「いつ届きますか」に答えるため |

形式の決め方：表にできる → CSV、1件の中に入れ子や長文がある → JSON、文章 → Markdown。

## つながり

`customer_id` が customers・inquiries・orders の3つをつなぐ。