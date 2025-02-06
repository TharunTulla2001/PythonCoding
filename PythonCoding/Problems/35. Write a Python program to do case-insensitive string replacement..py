text = input("Enter a string: ")
old_substring = input("Enter the substring to be replaced: ")
new_substring = input("Enter the new substring: ")

text_lower = text.lower()
old_substring_lower = old_substring.lower()  # Convert old_substring to lowercase
modified_text = text_lower.replace(old_substring_lower, new_substring)
print("Modified String:", modified_text)
'''
Enter a string: Tharun is a good boy
Enter the substring to be replaced: Tharun
Enter the new substring: chintu
Modified String: chintu is a good boy
'''
