set1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))
print(set1.difference(set2))

