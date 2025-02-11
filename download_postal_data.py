import os
import requests
import zipfile
import io
import csv
import pandas as pd

def download_and_extract_postal_data():
    # ダウンロードURL
    url = "https://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip"
    
    # データディレクトリの作成
    os.makedirs('data', exist_ok=True)
    
    try:
        # ZIPファイルのダウンロード
        print("郵便番号データをダウンロード中...")
        response = requests.get(url)
        response.raise_for_status()
        
        # ZIPファイルの展開
        print("データを展開中...")
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall('data')
        
        # CSVファイルの読み込みと変換
        print("データを処理中...")
        with open('data/KEN_ALL.CSV', 'r', encoding='shift_jis') as f:
            reader = csv.reader(f)
            data = list(reader)
        
        # DataFrameに変換
        df = pd.DataFrame(data, columns=[
            '全国地方公共団体コード',
            '旧郵便番号',
            '郵便番号',
            '都道府県名カナ',
            '市区町村名カナ',
            '町域名カナ',
            '都道府県名',
            '市区町村名',
            '町域名',
            '一町域複数番号',
            '小字毎番号',
            '大口事業所有無',
            '複数番号有無',
            '修正コード',
            '更新確認',
            '変更理由'
        ])
        
        # 必要なカラムのみを抽出
        df_simple = df[[
            '郵便番号',
            '都道府県名',
            '市区町村名',
            '町域名',
            '都道府県名カナ',
            '市区町村名カナ',
            '町域名カナ'
        ]]
        
        # JSONとして保存
        print("データをJSONとして保存中...")
        df_simple.to_json('data/postal_data.json', orient='records', force_ascii=False)
        
        print("完了！")
        return True
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return False

if __name__ == "__main__":
    download_and_extract_postal_data()