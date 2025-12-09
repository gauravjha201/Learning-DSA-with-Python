nums=[12,21,23,32,34,43,-9,98,-78,-67]
# nums.sort()
# print(nums[len(nums)-2])

#Approach 1  O(n)

# largest=float("-inf")
# secondlargest=float("-inf")
# for i in range(0,len(nums)-1):
#     largest=max(largest,nums[i])

# for i in range(0,len(nums)-1):
#     if nums[i]>secondlargest and nums[i]!=largest :
#         secondlargest=nums[i]

# print(secondlargest)

#Approach 2   O(n)

largest=float("-inf")
secondlargest=float("-inf")

for i in range(0,len(nums)-1):
    if nums[i]>largest :
        secondlargest=largest
        largest=nums[i]
        
    elif nums[i]!=largest and nums[i]>secondlargest :
            secondlargest=nums[i]

print(secondlargest)



