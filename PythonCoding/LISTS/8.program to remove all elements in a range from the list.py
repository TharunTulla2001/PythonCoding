start,end=list(map(int,input("Enter the numbers:").split()))
sample_list=[1,2,4,56,7,89]


for i in sample_list[start:end]:
    sample_list.remove(sample_list[start])
print(sample_list)
