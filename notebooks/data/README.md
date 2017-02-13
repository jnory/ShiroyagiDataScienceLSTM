# 演習用データセット

## 演習1 タクシーピックアップ予測
取得元: https://www.kaggle.com/fivethirtyeight/uber-pickups-in-new-york-city
取得時のライセンス: CC0

### train_enshu1.csv, test_enshu1.csv
取得元のデータから日別の乗車回数を集計したものです。
集計手順は、 `preprocess_enshu1.ipynb` に記載しています。

## 演習2 官公庁Q&Aコーパス

このデータはオープンデータとされているQ&Aを手動でかき集めてコーパス化したものです。

### QA.csv.gz
元データ

左から順に、出展URL, 収集日, タイトル, 質問, 回答 の順に並んでいます。
1行目はタイトルです。

全てのデータはCreative Commons Byの元に配布されているものです。

###  QA.normalized.csv.gz
データを綺麗にして、形態素解析したもの。
手順は、 `../preprocess_enshu2.ipynb` に記載しています。