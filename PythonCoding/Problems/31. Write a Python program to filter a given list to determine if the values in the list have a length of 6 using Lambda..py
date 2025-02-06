words = input("Enter words separated by spaces: ").split()
length_6_words = list(filter(lambda x: len(x) == 6, words))
print("Original List:", words)
print("Words with Length 6:", length_6_words)
'''
Enter words separated by spaces: yadagiri vijaya nirmala teja tharun
Original List: ['yadagiri', 'vijaya', 'nirmala', 'teja', 'tharun']
Words with Length 6: ['vijaya', 'tharun']
'''