# Sample dictionaries
d1 = {'0a0': 100, '0b0': 200, '0c0': 300}
d2 = {'0a0': 300, '0b0': 200, '0d0': 400}

result = {}
for key in d1:
    if key in d2:
        result[key] = d1[key] + d2[key]
    else:
        result[key] = d1[key]

for key in d2:
    if key not in result:
        result[key] = d2[key]

print("Combined Dictionary:", result)


#Combined Dictionary: {'0a0': 400, '0b0': 400, '0c0': 300, '0d0': 400}