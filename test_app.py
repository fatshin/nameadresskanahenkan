import unittest
from app import convert_name_to_kana, convert_address_to_kana

class TestKanaConversion(unittest.TestCase):
    def test_address_conversion(self):
        # 住所のテストケース
        test_cases = [
            {
                'input': '東京都港区芝１丁目１２－１９',
                'expected': 'トウキョウトミナトクシバ１チョウメ１２-１９'
            },
            {
                'input': '東京都渋谷区神宮前',
                'expected': 'トウキョウトシブヤクジングウマエ'
            }
        ]
        
        for case in test_cases:
            result = convert_address_to_kana(case['input'])
            self.assertEqual(result, case['expected'], 
                           f"住所変換エラー: 入力={case['input']}, 期待={case['expected']}, 実際={result}")

    def test_name_conversion(self):
        # 氏名のテストケース
        test_cases = [
            {
                'input': '本橋',
                'expected': 'モトハシ'
            },
            {
                'input': '伸一',
                'expected': 'シンイチ'
            }
        ]
        
        for case in test_cases:
            result = convert_name_to_kana(case['input'])
            self.assertEqual(result, case['expected'],
                           f"氏名変換エラー: 入力={case['input']}, 期待={case['expected']}, 実際={result}")

if __name__ == '__main__':
    unittest.main()