from flask import Flask, render_template, request
import pykakasi
import jaconv
import json
import os
import re
from openai import OpenAI
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

app = Flask(__name__)

# OpenAI APIの設定
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

# 名前データセットの読み込み
name_data = {}
name_chars = set()  # データセットに含まれる文字のセット
dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'names.json')
if os.path.exists(dataset_path):
    with open(dataset_path, 'r', encoding='utf-8') as f:
        name_data = json.load(f)
        # データセットに含まれる全ての文字を収集
        for name in name_data.keys():
            name_chars.update(list(name))

def get_reading_from_llm(name):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは日本語の名前の読み方を判定する専門家です。"},
                {"role": "user", "content": f"「{name}」という名前の一般的な読み方をカタカナで教えてください。余計な説明は不要です。"}
            ],
            temperature=0,
            max_tokens=50
        )
        kana = response.choices[0].message.content.strip()
        # 余計な文字を削除し、カタカナのみを抽出
        kana = re.sub(r'[^ァ-ヶー]', '', kana)
        return kana
    except Exception as e:
        print(f"LLM error: {e}")
        return None

def convert_name_to_kana(name):
    # データセットから名前を検索
    if name in name_data:
        # データセットに存在する場合はその読みを使用
        kana = name_data[name].get('kana', '')
        if kana:
            return kana
    
    # 名前に含まれる漢字がデータセットにない場合はLLMを使用
    has_unknown_char = any(
        char not in name_chars and re.match(r'[一-龯]', char)
        for char in name
    )
    
    if has_unknown_char:
        llm_result = get_reading_from_llm(name)
        if llm_result:
            return llm_result
    
    # それ以外の場合はpykakasiを使用
    kakasi = pykakasi.Kakasi()
    result = kakasi.convert(name)
    kana = ''.join([item['kana'] for item in result])
    return kana

def convert_address_to_kana(address):
    # 住所用の変換ロジック
    parts = []
    current = ''
    has_choume = False  # 「丁目」が既に処理されたかどうかのフラグ
    
    for char in address:
        if char.isdigit() or jaconv.z2h(char).isdigit():
            if current:
                # 現在の文字列を変換
                kakasi = pykakasi.Kakasi()
                result = kakasi.convert(current)
                parts.append(''.join([item['kana'] for item in result]))
                current = ''
            # 数字はそのまま保持
            parts.append(char)
        elif char in ['－', 'ー', '-']:
            if current:
                # 現在の文字列を変換
                kakasi = pykakasi.Kakasi()
                result = kakasi.convert(current)
                parts.append(''.join([item['kana'] for item in result]))
                current = ''
            parts.append('-')
        elif char in ['丁', '目']:
            if current:
                # 現在の文字列を変換
                kakasi = pykakasi.Kakasi()
                result = kakasi.convert(current)
                parts.append(''.join([item['kana'] for item in result]))
                current = ''
            if not has_choume and char == '丁':
                parts.append('チョウメ')
                has_choume = True
        else:
            current += char
    
    if current:
        # 残りの文字列を変換
        kakasi = pykakasi.Kakasi()
        result = kakasi.convert(current)
        parts.append(''.join([item['kana'] for item in result]))
    
    # 全体を結合
    kana = ''.join(parts)
    
    # 不要な空白を削除
    kana = re.sub(r'\s+', '', kana)
    
    return kana

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # フォームからデータを取得
        postal_code = request.form['postal_code']
        address = request.form['address']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        
        # カナ変換を実行
        address_kana = convert_address_to_kana(address)
        last_name_kana = convert_name_to_kana(last_name)
        first_name_kana = convert_name_to_kana(first_name)
        
        # 結果を表示
        return render_template('result.html',
                            postal_code=postal_code,
                            address=address,
                            address_kana=address_kana,
                            last_name=last_name,
                            last_name_kana=last_name_kana,
                            first_name=first_name,
                            first_name_kana=first_name_kana)
    
    # GETリクエストの場合はフォームを表示
    return render_template('form.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5002))
    app.run(host='0.0.0.0', port=port, debug=False)