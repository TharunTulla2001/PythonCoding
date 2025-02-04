set1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))
print(set1.isdisjoint(set2))

'''
Enter elements of first set (space-separated): 1 2 3 4 5
Enter elements of second set (space-separated): 6 7 8 9 10
True '''