input_dict = {1: [2, 3, 4], 2: [5, 6], 3: [7, 8, 9, 10]}

for key in input_dict:
    input_dict[key] = sum(input_dict[key])
print(input_dict)
