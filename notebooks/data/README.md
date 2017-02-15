# 演習用データセット

## 演習1 タクシーピックアップ予測
取得元: https://www.kaggle.com/fivethirtyeight/uber-pickups-in-new-york-city
取得時のライセンス: CC0

### train_enshu1.csv, test_enshu1.csv
取得元のデータから日別の乗車回数を集計したものです。
集計手順は、 `preprocess_enshu1.ipynb` に記載しています。

### hiden_no_tare_enshu1.{h5,json,logs.gz}
`../../scripts/create_hiden_no_tare_enshu1.py` を実行して得られた
10,000反復中の最高性能モデルとその学習ログです。
