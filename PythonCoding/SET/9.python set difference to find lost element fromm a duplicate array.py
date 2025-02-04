my_array=[1, 2, 3, 4, 5, 2]
my_set=set(my_array)
lost_item=[item for item in my_set if my_array.count(item)>1 ]
print(lost_item)
