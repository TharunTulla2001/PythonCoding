words = input("Enter words separated by spaces: ").split()
p_words = list(filter(lambda x: x.lower().startswith('p'), words))
if len(p_words) >= 2:
    print("Matched Words:", p_words[:2])
else:
    print("Not enough words starting with 'P'.")

'''
Enter words separated by spaces: Python Program coding practice play project
Matched Words: ['Python', 'Program']
'''
