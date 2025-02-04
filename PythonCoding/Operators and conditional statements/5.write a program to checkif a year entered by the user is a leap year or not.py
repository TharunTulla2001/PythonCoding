input_year = int(input("Enter the Year: "))
if (input_year % 4 == 0 & (input_year % 100 != 0 | input_year % 400 == 0)):
    print(f"Entered {input_year} is a Leap Year")
else:
    print(f"Entered {input_year} is not a Leap Year")
