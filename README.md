# coconara_ranking
coconaraサイトのサービスランキングを取得

## 背景
自分の出品したサービスの表示順位が何位なのかを知りたいため作成

## 概要
カテゴリーをクリックして表示されたページから最後のページまでクローリング
* タイトル
* サブタイトル
* 金額
* ユーザー

上記項目を抽出し、スプレッドシートに記載する

``` coconara_ranking.py

start_urls = ['https://coconala.com/categories/231?ref=header']
```
上記変数内の値をランキング表示したいカテゴリーのURLにすれば使えます。
