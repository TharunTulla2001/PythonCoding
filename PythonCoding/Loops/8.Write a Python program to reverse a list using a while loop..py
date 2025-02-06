list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_list = []
index = len(list_1) - 1

while index >= 0:
    reverse_list.append(list_1[index])
    index -= 1

print(reverse_list)  # Final reversed list
