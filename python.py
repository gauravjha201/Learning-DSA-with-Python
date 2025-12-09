from math import *
n=2234
num=n



# count=0
# n=5843
# while n>0:
#     count+=1
#     n=n//10    
# print(count)


# Approach 1
def countDigit(num):
    return int(log(num)+1)
print(countDigit())

