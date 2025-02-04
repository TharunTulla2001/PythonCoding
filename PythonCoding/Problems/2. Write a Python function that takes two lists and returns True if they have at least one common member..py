def compare(list_1, list_2):
    for num in list_1:
        if num in list_2:
            return True
    return False

list_1=list(map(int,input("enter the numbers of list1:").split()))
list_2=list(map(int,input("enter the numbers of list2:").split()))
print(compare(list_1,list_2))