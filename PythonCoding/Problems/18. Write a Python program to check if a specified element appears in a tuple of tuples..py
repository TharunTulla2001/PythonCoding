tuple_of_tuples = (("Red", "White", "Blue"), ("Green", "Pink", "Purple"), ("Orange", "Yellow", "Lime"))

def check_element_exists(tuples, element):
    for sub_tuple in tuples:
        if element in sub_tuple:
            return True
    return False

element_to_check = input("Enter the element to check: ")

result = check_element_exists(tuple_of_tuples, element_to_check)
print(f"Check if '{element_to_check}' is present in the tuple of tuples:", result)
