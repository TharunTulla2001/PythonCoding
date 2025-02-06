n = 6  # Size of the heart

# Upper part (Inverted Heart)
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(1, i * 2):
        if j == 1 or j == (i * 2 - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Lower part (Pointed Tip)
for i in range(1, n // 2 + 2):
    for j in range(n - 2):
        print(" ", end=" ")
    print("*")
