str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
set1 = set(str1.split())
set2 = set(str2.split())
uncommon_words = set1.symmetric_difference(set2)
print("Uncommon words:", uncommon_words)
'''
Enter first string: apple banana mango
Enter second string: banana orange mango
Uncommon words: {'orange', 'apple'}
'''