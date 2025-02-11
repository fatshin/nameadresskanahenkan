# 住所・氏名カナ変換アプリ

日本語の住所と氏名をカタカナに変換するWebアプリケーションです。

## 特徴

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

## 使用方法

1. アプリケーションを起動
```bash
python app.py
```

2. ブラウザで `http://localhost:5002` にアクセス

3. フォームに住所と氏名を入力して変換

## デプロイ

このアプリケーションは以下のプラットフォームにデプロイ可能です：

- Heroku
- Railway
- Render
- その他のPythonをサポートするプラットフォーム

## ライセンス

MIT License

## 謝辞

- [japanese-personal-name-dataset](https://github.com/shuheilocale/japanese-personal-name-dataset) - 日本人名データセット
- [pykakasi](https://github.com/miurahr/pykakasi) - 漢字からカナへの変換
- [jaconv](https://github.com/ikegami-yukino/jaconv) - 文字種の変換