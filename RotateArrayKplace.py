nums=[2,3,5,7,3,6,9,2]
k=5 #number of element from end


# #Approach (BF method)
# n=len(nums)
# rotation=k%n

# for _ in range(0,rotation):
#     e=nums.pop()
#     nums.insert(0,e)
# print(nums)



# #Approach 1
# n=len(nums)
# k =k%n

# nums[:]=nums[n-k:]+nums[:n-k]
# print(nums)


#Approach 2
n=len(nums)
def reverse(nums,left,right):
    while(left<right):
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)

print(nums)
