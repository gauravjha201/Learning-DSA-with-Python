# BF approach

# str="abcdef"
# n=len(str)
# def palin(str,left,right):
#     while left<right :
#         if str[left]!=str[right] :
#             return False
#             left+=1
#             right-+1
#         else:
#             return True
# print(palin(str,0,n-1))

#recursion
string="abcddcba"
def palin(string,left,right):
    if left>=right :
        return True
    if string[left]!=string[right]:
        return False

    return palin(string,left+1,right-1)

print(palin(string,0,len(string)-1))

