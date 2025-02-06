text = input("Enter a sentence: ")
words = text.split()
long_words = list(filter(lambda x: len(x) >= 4, words))
print("Words with at least 4 characters:", long_words)
'''
Enter a sentence: tharun is a good boy
Words with at least 4 characters: ['tharun', 'good']
'''