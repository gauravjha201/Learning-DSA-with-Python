nums=[2,3,4,5,6,7,8,9,10,11,12]
target=9
def binary_search_iterative(nums,target):#log(n)
    low=0
    high=len(nums)-1
    
    while low<=high :
        mid=(low+high)//2
        if nums[mid]==target :
            return mid
        elif nums[mid]>target :
            high=mid-1
        else:
            low=mid+1
    return -1

# print(binary_search_iterative(nums,9))

def binary_search_recursive(nums,target,low,high):
    if low >high :
        return -1
    mid=(low+high)//2
    if nums[mid]==target :
        return mid 
    elif nums[mid]>target :
        return binary_search_recursive(nums,target,low,mid-1)
    else:
        return binary_search_recursive(nums,target,mid+1,high)

print(binary_search_recursive(nums,9,0,len(nums)-1))




