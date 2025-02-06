words = input("Enter words separated by spaces: ").split()
search_word = input("Enter the word to search: ")
matches = [word for word in words if word == search_word]
if matches:
    print(f"Found {len(matches)} matches:", matches)
else:
    print("No matches found.")
'''
Enter words separated by spaces: tharun chintu pandu tharun
Enter the word to search: tharun
Found 2 matches: ['tharun', 'tharun']
'''