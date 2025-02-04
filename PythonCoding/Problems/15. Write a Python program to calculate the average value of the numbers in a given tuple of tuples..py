data = ((10, 10, 10, 12),(30, 45, 56, 45),(81, 80, 39, 32),(1, 2, 3, 4))
#average= [sum(col) / len(col) for col in zip(*data)]

averages = []
columns = list(zip(*data))

for col in columns:
    avg = sum(col) / len(col)
    averages.append(avg)

print("Average value of the numbers:", averages)

#Average value of the numbers: [30.5, 34.25, 27.0, 23.25]