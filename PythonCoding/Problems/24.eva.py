str1=input("enter the sring")
box=" "
if str1.isdigit():
    middle_index=len(str1)//2
    box=str1[middle_index]
print(box)