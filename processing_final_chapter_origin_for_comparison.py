import re

# ファイルの読み込み
input_path = 'test_data_only_final_chapter_origin.txt'
output_path = 'test_data_only_final_chapter_origin_for_comparison.txt'

# 文に分割し、それぞれを改行で区切る処理を行う
def process_text(text):
    # 文を分割する正規表現（句読点で分割されず、ピリオド、感嘆符、疑問符で文を終了）
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # 処理後の文を格納するリスト
    processed_sentences = []
    for sentence in sentences:
        # 句読点を含む記号を削除し、単語のみを残す
        cleaned_sentence = re.sub(r'[^\w\s]', '', sentence)
        # 不要な空白を削除し、単語間にスペースを挿入
        cleaned_sentence = ' '.join(cleaned_sentence.split())
        processed_sentences.append(cleaned_sentence)
    return processed_sentences

# テキストファイルを読み込み、処理後の文を新しいファイルに保存
with open(input_path, 'r', encoding='utf-8') as file:
    text = file.read()
    processed_sentences = process_text(text)

with open(output_path, 'w', encoding='utf-8') as file:
    for sentence in processed_sentences:
        file.write(sentence + '\n\n')  # 文ごとに2つの改行を追加

print(f"Processed file has been saved to: {output_path}")
