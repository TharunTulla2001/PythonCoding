input_list=[1,2,3,4,5]
print(len(input_list))
print("Using While Loop")
# 1)using while loop
i=0
while i<len(input_list):
    print(input_list[i])
    i+=1
 # 2)using for in loop
print("Using For in Loop")
for i in input_list:
    print(i)
# Using Builtin Methods
# 1)print method
print(input_list)
# 2)join method
print("Using Join Method")
input_string=["apple","banana","Cabbage"]
print(','.join(input_string))
#3)Enumerate method
print("Using Enumerate Method")
for index,item in enumerate(input_list):
    print(f"The Index of {index} has item {item}")
    