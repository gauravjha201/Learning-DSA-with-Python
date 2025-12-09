nums=[5,3,4,1,5,9,6,-1,2]
def insertion(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key



insertion(nums)
print(nums)