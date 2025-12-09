nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
n=len(nums)
target=3
def countOccurrence(nums ,target):# this is brute force approach
    count=0
    for i in range(0,n):
        if nums[i]==target:
            count+=1
    return count
# print(countOccurrence(nums,target))

# def countOccurence1(nums,target):#this is optimal approach 
#     low=0
#     high=n-1
#     first=-1
#     last=n
#     while low<=high :
#         mid=(low+high)//2
#         if nums[mid]>=target :
#             first=mid
#             high=mid-1
#         else:
#             low=mid+1
#     if first==-1:
#         return 0
#     else:
#         while low<=high :
#             mid=(low+high)//2
#             if nums[mid]>target :
#                 last=mid
#                 high=mid-1
#             else:
#                 low=mid+1
#         return last,first
    
# print(countOccurence1(nums,target))





def lowerBound(nums,target):
    lower=-1
    low=0
    high=n-1
    while low<=high :
        mid=(low+high)//2
        if nums[mid]>=target :
            lower=mid
            high=mid-1
        else:
            lower=mid+1
        return lower
        
def upperBound(nums,target):
    upper=-1
    low=0
    high=n-1
    while low<=high :
        mid=(low+high)//2
        if nums[mid]>target:
            upper=mid
            high=mid -1
        else:
            lower=mid+1
        return upper
        
lower=lowerBound(nums,target)
if lower==-1:
    print(0)
else:
    upper=upperBound(nums,target)
    print(lower,upper)





