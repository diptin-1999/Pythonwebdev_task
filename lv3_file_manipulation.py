def count_word_occurrences(file_path):
    word_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower() 
                word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def display_word_counts(word_counts):
    sorted_words = sorted(word_counts.items(), key=lambda x: x[0])
    for word, count in sorted_words:
        print(f"{word}: {count}")

def main():
    file_path = input("Enter the path to the text file: ")
    try:
        word_counts = count_word_occurrences(file_path)
        print("Occurrences of each word in alphabetical order:")
        display_word_counts(word_counts)
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")

if __name__ == "__main__":
    main()
