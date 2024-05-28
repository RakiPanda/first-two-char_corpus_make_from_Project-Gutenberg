import re

# テキストファイルの読み込み
file_path = '84.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 最後の "Chapter" を見つける
start_last_chapter = text.rfind("Chapter")  # "Chapter" の最後の出現位置を見つける
last_chapter_text = text[start_last_chapter:]  # 最後の "Chapter" からテキストを抽出する

# 最後の "Chapter" を文章ごとに分割
sentences = re.split(r'(?<=[.!?])\s+', last_chapter_text)

# 各文章を処理
concatenated_result = []
for sentence in sentences:
    words = re.findall(r'\b\w+\b', sentence)
    # 各単語の最初の2文字を連結する。単語が1文字の場合、スペースを追加せずそのまま使用
    processed_words = [word[:2] for word in words]
    concatenated_result.append(''.join(processed_words))

# 結果をテキストファイルに保存
output_path = 'test_data_only_final_chapter.txt'
with open(output_path, 'w', encoding='utf-8') as output_file:
    for result in concatenated_result:
        output_file.write(result + "\n")

print("ファイルが保存されました:", output_path)
