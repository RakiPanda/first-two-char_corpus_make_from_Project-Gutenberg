import re
import csv
import matplotlib.pyplot as plt

def read_and_process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        sentences = file.read().strip().split('\n\n')
        return [(re.sub(r'[^\w\s]', '', sentence).lower().split(), sentence) for sentence in sentences]

def calculate_accuracy(original, estimated):
    total = len(original)
    if total == 0:
        return 0
    matches = sum(1 for o, e in zip(original, estimated) if o == e)
    return (matches / total) * 100

# File paths
original_path = 'test_data_only_final_chapter_origin_for_comparison_84.txt'
estimated_path = 'estimated_sentence_from_test_data_84_by_1342-0mod.txt'
output_csv_path = '84_accuracy_by_1342-0mod.csv'

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
    writer.writerow(['Average Accuracy', f'{average_accuracy:.2f}'])
    writer.writerow(['Sentence Index', 'Original Sentence', 'Estimated Sentence', 'Accuracy (%)'])
    for index, (original, estimated, accuracy) in enumerate(accuracies, 1):
        writer.writerow([index, original, estimated, accuracy])

# Plotting the histogram of accuracies
accuracy_values = [acc[2] for acc in accuracies]
plt.hist(accuracy_values, bins=10, edgecolor='black')
plt.title('Accuracy Distribution 84 test data by 1342-0 mod')
plt.xlabel('Accuracy (%)')
plt.ylabel('Number of Sentences')
plt.grid(True)
plt.savefig('accuracy_histogram_84_by_1342-0mod.png')
plt.show()

print(f'Accuracy results have been saved to {output_csv_path}')
print('Histogram of accuracy distribution has been saved as "accuracy_histogram_84_by_1342-0mod.png".')
