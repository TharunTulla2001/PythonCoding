my_list=[0,2,5,1,9,8,10]
n=len(my_list)

#ascending
# print(sorted(my_list))
for i in range(len(my_list)):
    for j in range(0,n-i-1):
        if my_list[j]>my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
print(my_list)
#descending
for i in range(len(my_list)):
    for j in range(0,n-i-1):
        if my_list[j]<my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
print(my_list)