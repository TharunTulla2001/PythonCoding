def count_case_letters(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

user_string = input("Enter a string: ")
count_case_letters(user_string)
'''
Enter a string: Tharun Yadav
Uppercase letters: 2
Lowercase letters: 9 '''