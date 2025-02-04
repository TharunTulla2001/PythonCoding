tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)

element_wise_sum = tuple(sum(values) for values in zip(tuple1, tuple2, tuple3))
print("Element-wise sum of the said tuples:", element_wise_sum)

#Element-wise sum of the said tuples: (6, 9, 8, 6)