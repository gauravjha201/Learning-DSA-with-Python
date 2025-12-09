nums=[2,5,7,9,4,2,7,8]

#Approach 1
n=len(nums)
nums1=nums[n-1]+nums[0:n-1]
print(nums1)




#Approach 

# n=len(nums)
# def rotate():
#     j=nums[n-1]
#     for i in range (n-2,-1,-1):
#         nums[i+1]=nums[i]
#     nums[0]=j
# rotate()
# print(nums)
