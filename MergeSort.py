nums=[7,3,1,9,2,6,5,4,10]
def merge(nums1,nums2):
    result=[]
    n=len(nums1)
    m=len(nums2)
    i,j=0,0
    while i<n and j<m:
        if nums1[i]<=nums2[j] :
            result.append(nums1[i])
            i+=1
        else:
            result.append(nums2[j])
            j+=1
    while i<n:
        result.append(nums1[i])
        i+=1
    while j <m:
        result.append(nums2[j])
        j+=1
    return result
def mergesort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    nums1=nums[:mid]
    nums2=nums[mid:]
    nums1=mergesort(nums1)
    nums2=mergesort(nums2)
    return merge(nums1,nums2)
print(mergesort(nums))
