input_string=input("Enter the string:")
is_alpha=any(char.isalpha() for char in input_string)
if  is_alpha:
    print("Valid String")
else:
    print("Please include at least alphabet")
