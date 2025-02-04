def longest_word(input_num):
    big_word=input_num[0]
    for i in range(1,len(input_num)):
     if input_num[i]>big_word:
         big_word=input_num[i]
         return big_word

input_num=list(map(str,input("enter the num:").split()))
print(longest_word(input_num))