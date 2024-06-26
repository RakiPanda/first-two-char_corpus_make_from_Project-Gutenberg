import re
import csv

def read_and_process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        # Read the file and split into sentences by double newline
        sentences = file.read().strip().split('\n\n')
        # Return both cleaned and original sentences
        return [(re.sub(r'[^\w\s]', '', sentence).lower().split(), sentence) for sentence in sentences]

def calculate_accuracy(original, estimated):
    total = len(original)
    if total == 0:
        return 0
    matches = sum(1 for o, e in zip(original, estimated) if o == e)
    return (matches / total) * 100

# File paths
original_path = 'test_data_only_final_chapter_origin_for_comparison_1342-0.txt'
estimated_path = 'estimated_sentence_from_test_data_1342-0.txt'
output_csv_path = '1342-0_accuracy.csv'

# Process files
original_data = read_and_process_file(original_path)
estimated_data = read_and_process_file(estimated_path)

# Calculate accuracy for each sentence
accuracies = []
for (original_words, original_sentence), (estimated_words, estimated_sentence) in zip(original_data, estimated_data):
    accuracy = calculate_accuracy(original_words, estimated_words)
    accuracies.append((original_sentence, estimated_sentence, accuracy))

# Calculate average accuracy
average_accuracy = sum(acc[2] for acc in accuracies) / len(accuracies) if accuracies else 0

# Write accuracies and sentences to a CSV file
with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write headers
    writer.writerow(['Average Accuracy', f'{average_accuracy:.2f}'])
    writer.writerow(['Sentence Index', 'Original Sentence', 'Estimated Sentence', 'Accuracy (%)'])
    for index, (original, estimated, accuracy) in enumerate(accuracies, 1):
        writer.writerow([index, original, estimated, accuracy])

print(f'Accuracy results have been saved to {output_csv_path}')
