numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
divisible_numbers = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))
print("Original List:", numbers)
print("Numbers Divisible by 19 or 13:", divisible_numbers)
'''
Enter numbers separated by spaces: 13 19 26 38 57 76 95 100 114 133 190
Original List: [13, 19, 26, 38, 57, 76, 95, 100, 114, 133, 190]
Numbers Divisible by 19 or 13: [13, 19, 26, 38, 57, 76, 95, 114, 133, 190]
'''

