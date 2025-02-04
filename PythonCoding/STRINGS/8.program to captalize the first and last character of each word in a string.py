input_string = input("Enter the string: ")
output = ""

for i in input_string.split():
    if len(i) > 1:
        output += i[0].upper() + i[1:-1].lower() + i[-1].upper() + " "
    else:
        output += i.upper() + " "

print(output)
