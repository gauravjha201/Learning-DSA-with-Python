nums=[1,2,3,10,5,6,7,8]
n=len(nums)
def isSorted():

    for i in range(0,n-1):
        if nums[i]>nums[i+1] :
            return False
        return True
        
print(isSorted())
