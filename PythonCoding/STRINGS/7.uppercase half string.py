input_string = input("Enter the string: ")
mid_index = len(input_string) // 2
first_half = input_string[:mid_index]
second_half = input_string[mid_index:]
output = first_half.upper() + second_half
print(output)
