def check_leap_year(yea):
    if (yea % 4 == 0 and (yea % 100 != 0 or yea % 400 == 0)):
        return "Leap Year"
    else:
        return "Not a Leap Year"
year=int(input("Enter the Year:"))
print(check_leap_year(year))