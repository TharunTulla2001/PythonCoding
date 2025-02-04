my_dict = {
    1: "apple",
    "name": "John",
    (2, 3): "tuple key"
}
keys=[]
values=[]
key_value_pairs=[]
for key,value in my_dict.items():
    keys.append(key)
    values.append(value)
    key_value_pairs.append((key,value))
print("Keys in my_dict:",keys)
print("values in my_dict:",values)
print("Key value pairs:",key_value_pairs)