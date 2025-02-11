たい# 住所・氏名カナ変換アプリ

日本語の住所と氏名をカタカナに変換するWebアプリケーションです。

## 特徴

- 郵便番号からの住所自動入力と読み仮名変換
- 住所のカナ変換
- 氏名のカナ変換（日本人名データセット使用）
- データセットにない漢字はAI（GPT-3.5）を使用して変換
- シンプルなWebインターフェース

## 必要条件

- Python 3.8以上
- OpenAI API キー

## インストール方法

1. リポジトリをクローン
```bash
git clone https://github.com/yourusername/kanahenkan.git
cd kanahenkan
```

2. 必要なパッケージをインストール
```bash
pip install -r requirements.txt
```

3. 環境変数の設定
```bash
cp .env.example .env
```
`.env`ファイルを編集し、OpenAI APIキーを設定してください。

4. 郵便番号データのダウンロード
```bash
python download_postal_data.py
```
このスクリプトは日本郵便が提供する郵便番号データをダウンロードし、必要な形式に変換します。

## 使用方法

1. アプリケーションを起動
```bash
python app.py
```

2. ブラウザで `http://localhost:5002` にアクセス

3. フォームに郵便番号、住所、氏名を入力して変換
   - 郵便番号を入力すると、対応する住所とその読み仮名が自動的に入力されます
   - 郵便番号が見つからない場合は、手動で入力した住所を変換します

## データソース

- [郵便番号データ](https://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip) - 日本郵便株式会社
- [japanese-personal-name-dataset](https://github.com/shuheilocale/japanese-personal-name-dataset) - 日本人名データセット

## デプロイ

このアプリケーションは以下のプラットフォームにデプロイ可能です：

- Heroku
- Railway
- Render
- その他のPythonをサポートするプラットフォーム

デプロイ時の注意点：
- 郵便番号データは定期的に更新されます。本番環境では定期的なデータ更新の仕組みを実装することをお勧めします。
- APIキーは必ず環境変数として設定してください。

## ライセンス

MIT License

## 謝辞

- 日本郵便株式会社 - 郵便番号データの提供
- [japanese-personal-name-dataset](https://github.com/shuheilocale/japanese-personal-name-dataset) - 日本人名データセット
- [pykakasi](https://github.com/miurahr/pykakasi) - 漢字からカナへの変換
- [jaconv](https://github.com/ikegami-yukino/jaconv) - 文字種の変換