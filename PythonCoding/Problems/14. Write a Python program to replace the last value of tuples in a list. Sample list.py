tuple_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
modified_list = [t[:-1] + (100,) for t in tuple_list]
print("Updated List:", modified_list)

#Updated List: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]