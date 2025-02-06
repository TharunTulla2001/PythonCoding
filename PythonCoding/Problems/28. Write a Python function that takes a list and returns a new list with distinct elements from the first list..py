def get_distinct_elements(lst):
    return list(set(lst))

user_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("List with distinct elements:", get_distinct_elements(user_list))
'''
Enter numbers separated by spaces:  2 4 6 4 3  6 7 1 3 7 4 5 6 1 
List with distinct elements: [1, 2, 3, 4, 5, 6, 7]
'''