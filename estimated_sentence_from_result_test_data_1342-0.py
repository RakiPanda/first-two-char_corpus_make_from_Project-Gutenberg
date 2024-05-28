import re

# ファイルの読み込み
input_path = 'result_test_data_only_final_chapter_ver_no_UNK_1342-0.txt'
output_path = 'estimated_sentence_from_test_data_1342-0.txt'

with open(input_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 推定された元の単語を抽出
extracted_lines = []
for line in lines:
    # 各行から "/<word>" を抽出して連結
    extracted_words = re.findall(r'/(?P<word>\b\w+\b)', line)
    extracted_line = ' '.join(extracted_words)
    extracted_lines.append(extracted_line + '\n')

# 抽出したテキストを新しいファイルに保存
with open(output_path, 'w', encoding='utf-8') as file:
    file.writelines(extracted_lines)

print(f"ファイルが保存されました: {output_path}")
