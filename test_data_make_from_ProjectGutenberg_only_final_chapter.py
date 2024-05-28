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

# 各文章を処理して最初の2文字だけの結果を保存
concatenated_result = []
for sentence in sentences:
    words = re.findall(r'\b\w+\b', sentence)
    processed_words = [word[:2] for word in words]  # 各単語の最初の2文字を連結
    concatenated_result.append(''.join(processed_words))

# 最初の2文字だけの結果をファイルに保存
output_path_short = 'test_data_only_final_chapter.txt'
with open(output_path_short, 'w', encoding='utf-8') as output_file:
    for result in concatenated_result:
        output_file.write(result + "\n")

# 元の文章をファイルに保存
output_path_full = 'test_data_only_final_chapter_origin.txt'
with open(output_path_full, 'w', encoding='utf-8') as output_file:
    for sentence in sentences:
        output_file.write(sentence + "\n")

print("最初の2文字だけの結果が保存されました:", output_path_short)
print("元の文章が保存されました:", output_path_full)
