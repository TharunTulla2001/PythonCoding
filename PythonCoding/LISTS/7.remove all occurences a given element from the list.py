my_list=[1,2,4,3,4,5,5]
my_number=5

for item in my_list[:]:
    if item==my_number:
        my_list.remove(my_number)
print(my_list)