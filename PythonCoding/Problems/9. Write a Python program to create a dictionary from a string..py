input_string=input("Enter the String:")
letters_count={}
for i in input_string:
    if i in letters_count:
        letters_count[i]+=1
    else:
        letters_count[i]=1
print(letters_count)

'''
Enter the String:tharun
{'t': 1, 'h': 1, 'a': 1, 'r': 1, 'u': 1, 'n': 1}'''