def reverse_sublist(list_input, start):
    list_input[start:] = list_input[start:][::-1]
    return list_input
list_input= list(map(int, input("Enter the list of numbers: ").split()))
start_index = int(input("Enter the start index for reverse: "))
print(reverse_sublist(list_input, start_index))

'''Enter the list of numbers: 1 2 3 4 5 6 7 8 9 
Enter the start index for reverse: 4
[1, 2, 3, 4, 9, 8, 7, 6, 5]'''
