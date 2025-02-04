input_str=input("Enter the String:")
output=""
for i in input_str:
    if i!=" ":
        output+=i
print("Length of string avoiding spaces:",len(output),output)

