text = input("Enter a string: ")
i = int(input("Enter the index to remove: "))
new_text = text[:i] + text[i+1:]
print("Modified String:", new_text)
'''
Enter a string: tharun
Enter the index to remove: 0
Modified String: harun
'''