numbers_dict = {
    "a": [1, 2, 3, 4, 5],
    "b": [10, 15, 20, 25, 30],
    "c": [7, 8, 9, 10],
    "d": [12, 14, 17, 19]
}
filtered_dict = {}
for key, values in numbers_dict.items():
    even_numbers = []
    for num in values:
        if num % 2 == 0:
            even_numbers.append(num)
    filtered_dict[key] = even_numbers
print("even numbers are:",filtered_dict)