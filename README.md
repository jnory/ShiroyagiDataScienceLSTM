# 使い方

## コンテナビルド
> ./note build

## コンテナ起動
> ./note run

## コンテナ停止
> ./note rm

## 独自のSLL証明書を使いたい
デフォルトではオレオレ証明書を使います。
`config/keys` 配下に、 `jupyter.key` と `jupyter.pem` を置くことで、
証明書を切り替えることができます。