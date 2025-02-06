is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
prime_numbers = list(filter(is_prime, numbers))

print("Original List:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
print("Prime Numbers:", prime_numbers)
'''
Enter numbers separated by spaces: 1 2 3 4 5 6 7 8 9 
Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Even Numbers: [2, 4, 6, 8]
Odd Numbers: [1, 3, 5, 7, 9]
Prime Numbers: [2, 3, 5, 7]
'''
