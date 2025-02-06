numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

square = list(map(lambda x: x**2, numbers))
cube = list(map(lambda x: x**3, numbers))

print("Original List:", numbers)
print("Squared List:", square)
print("Cubed List:", cube)

'''
Enter numbers separated by spaces: 1 2 3 4 5 
Original List: [1, 2, 3, 4, 5]
Squared List: [1, 4, 9, 16, 25]
Cubed List: [1, 8, 27, 64, 125]
'''