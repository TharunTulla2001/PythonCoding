def count_words(filename):
    with open(filename, "r") as file:
        text = file.read().lower()  # Read file and convert to lowercase

    words = text.split()  # Split text into words
    word_count = {}  # Dictionary to store word frequencies

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1  # Count words

    for word, count in word_count.items():
        print(word, ":", count)

# Example usage
count_words("file.txt")  # Replace with your file name
'''
hi : 1
how : 1
are : 1
you : 1
'''