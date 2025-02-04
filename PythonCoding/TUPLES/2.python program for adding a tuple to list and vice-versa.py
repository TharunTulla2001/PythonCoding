my_tuple=("tharun",24,True)
List=["THARUN",48,False]
#tuple to list
convert_to_list=list(my_tuple)
List.extend(convert_to_list)
#print(List)

#list to tuple

convert_to_tuple=tuple(List)
my_tuple+=convert_to_tuple
print(my_tuple)
