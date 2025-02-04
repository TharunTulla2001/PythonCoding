def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])
input_string = input("Enter tuples as a list: ")
user_list = eval(input_string)
sorted_list = sort_by_last_element(user_list)
print("Sorted List:", sorted_list)
#Enter tuples as a list: (2, 5),(1, 2),(4, 4),(2, 3),(2, 1)
#Sorted List: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]