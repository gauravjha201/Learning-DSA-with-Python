nums=[1,1,1,2,2,2,3,3,4,4,4,5,5,6,7,7,7,8,9,10,11,12]
target=4
def Lower_Bound(nums,target):
    n=len(nums)
    lower_bound=n
    low=0
    high=n-1
    while low<=high :
        mid=(low+high)//2
        if nums[mid]>=target :
            lower_bound=mid
            high=mid-1
        else:
            low=mid+1
    return lower_bound
print(Lower_Bound(nums,target))

def Upper_Bound(nums,target):
    n=len(nums)
    upper_bound=n
    low=0
    high=n-1
    while low<=high :
        mid=(low+high)//2
        if nums[mid]<=target :
            upper_bound=mid
            low=mid+1
        else:
            high=mid-1
    return upper_bound
print(Upper_Bound(nums,target))

    
