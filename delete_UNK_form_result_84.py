import re

# ファイルの読み込み
input_path = 'result_test_data_only_final_chapter_84.txt'
output_path = 'result_test_data_only_final_chapter_ver_no_UNK_84.txt'

with open(input_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# "/UNK" が単独で存在する行を検出し、代わりに改行を挿入
cleaned_lines = [line if not re.match(r'^/UNK\s*$', line) else '\n' for line in lines]

# 結果を新しいファイルに書き込み
with open(output_path, 'w', encoding='utf-8') as file:
    file.writelines(cleaned_lines)

print(f"ファイルが保存されました: {output_path}")
