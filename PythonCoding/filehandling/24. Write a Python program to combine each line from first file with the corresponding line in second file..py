with open("file.txt") as f1, open("file2.txt") as f2, open("output.txt", "w") as out:
    for line1, line2 in zip(f1, f2):
        out.write(line1.strip() + " " + line2.strip() + "\n")  # Combine and write

print("Files combined successfully!")
'''
hi hello
how are you i am fine
(combination of two files content side by side)

'''