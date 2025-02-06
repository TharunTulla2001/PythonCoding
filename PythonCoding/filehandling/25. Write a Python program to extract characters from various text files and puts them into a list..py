char_list = []

with open("file.txt") as f1, open("file2.txt") as f2:  # Open multiple files
    char_list.extend(f1.read())  # Read and add characters
    char_list.extend(f2.read())

print(char_list)  # Print extracted characters
'''
['h', 'i', '\n', 'h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '\n', 'h', 'e', 'l', 'l', 'o', '\n', 'i', ' ', 'a', 'm', ' ', 'f', 'i', 'n', 'e']
'''