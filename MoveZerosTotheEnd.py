nums=[1,2,0,4,3,0,0,4,5,0,5]

# BF Approach T.C=O(n) S.C =O(n)
# n=len(nums)
# temp=[]
# for i in range(0,n):
#     if nums[i] !=0 :
#         temp.append(nums[i])
# n2=len(temp)
# for i in range(n2):
#     nums[i]=temp[i]
# for i in range(n2,n):
#     nums[i]=0

# print(nums)



#Approach 1 T.C=O(n) S.C=O(1)
n=len(nums)
if n==1 :
    print(nums)
i=0
while i <n :
    if nums[i]==0 :
        break
    i+=1
if i==n :
    print(nums)
j=i+1
while j<n:
    if nums[j]!=0 :
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
    j+=1

print(nums)




