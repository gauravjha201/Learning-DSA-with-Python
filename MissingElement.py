nums=[9,7,6,4,5,2,3,1,0]
n=len(nums)

#BF approach
# for i in range(0,n+1):
#     if i not in nums :
#         print(i)


#better approach
freq_dic={}
for i in range(0,n+1):
    freq_dic[i]=0
for num in nums :
    freq_dic[num]=1

for key,value in freq_dic.items():
    if value!=1:
        print(key)  



#Optimal approach
# actualsum=(n*(n+1))//2
# sum=0
# for i in range(0,n) :
#     sum=sum+nums[i]
# print(sum)
# print(actualsum)

# print(actualsum-sum)

