def min_sum_subsequence(list_input):
    list_input.sort()
    subsequence = list_input[:]
    return subsequence, sum(subsequence)
list_input= list(map(int, input("Enter the list of numbers: ").split()))
subsequence, total_sum = min_sum_subsequence(list_input)
print("Minimum sum subsequence:", subsequence)
print("Sum of subsequence:", total_sum)
'''
Enter the list of numbers: 1 2 3 -6 -9 4 5
Minimum sum subsequence: [-9, -6, 1, 2, 3, 4, 5]
Sum of subsequence: 0 '''
