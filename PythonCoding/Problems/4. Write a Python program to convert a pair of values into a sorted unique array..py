def sorted_unique_array(list_1, list_2):
    combined_list = list_1 + list_2
    unique_list = []
    for item in combined_list:
        if item not in unique_list:
            unique_list.append(item)
    unique_list.sort()
    return unique_list
list_1 = list(map(int, input("Enter the first pair numbers: ").split()))
list_2 = list(map(int, input("Enter the second pair numbers: ").split()))
print(sorted_unique_array(list_1, list_2))
