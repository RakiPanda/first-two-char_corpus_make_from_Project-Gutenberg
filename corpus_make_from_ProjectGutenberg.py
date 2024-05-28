import re

# ファイルの読み込み
file_path = '84.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 不要な部分を削除 (Gutenberg の前後の説明部分など)
start_marker = "*** START OF THIS PROJECT GUTENBERG EBOOK FRANKENSTEIN ***"
end_marker = "*** END OF THIS PROJECT GUTENBERG EBOOK FRANKENSTEIN ***"
start_index = text.find(start_marker) + len(start_marker)
end_index = text.find(end_marker)
clean_text = text[start_index:end_index]

# 文ごとに処理し、各単語の最初の2文字とその単語を '/' で連結
sentences = re.split(r'(?<=[.!?])\s+', clean_text)
training_data = []
for sentence in sentences:
    words = re.findall(r'\b\w+\b', sentence)  # 単語を抽出し、元の大文字小文字を保持
    training_sentence = ' '.join([f"{word[:2]}/{word}" for word in words])
    training_data.append(training_sentence)

# ファイルに保存
output_path = 'first-two-char_corpus_from84.txt'
with open(output_path, 'w', encoding='utf-8') as file:
    for entry in training_data:
        file.write(f"{entry}\n")
