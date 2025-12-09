nums=[1,2,3,4,5,6,7,8,10,11,13,16,19]
n=len(nums)

def floor_ceil(nums,target):
    floor=-1
    ceil=-1
    low=0
    high=n-1
    while low<=high :
        mid=(low+high)//2
        if nums[mid]==target :
            return [nums[mid],nums[mid]]
        elif nums[mid]>target :
            ceil=nums[high]
            high=mid-1
        else:
            floor=nums[low]
            low=mid+1
    return [floor,ceil]


print(floor_ceil(nums,12))

    