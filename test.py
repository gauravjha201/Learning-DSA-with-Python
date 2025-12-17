# #count number of subset of sum of target
# nums=[5,9,4,1]
# target=9
# def backtrack(index,total):
#     if total==target:
#         return 1
#     if total>target : 
#         return 0
#     if index>=len(nums):
#         return 0
#     sum=total+nums[index]
#     pick=backtrack(index+1,sum)
#     sum=total
#     non_pick=backtrack(index+1,sum)
#     return pick+non_pick

# print(backtrack(0,0))


# nums=[8,1,5,2,9,0,3,4]
# def merge_sort(nums):
#     if len(nums)==1:
#         return 
#     n=len(nums)
#     mid=n/2
#     nums1=nums[:mid]
#     nums2=nums[mid:]
#     nums1=merge_sort(nums1)
#     nums2=merge_sort(nums2)
#     return merge(nums1,nums2)



# def merge(nums1,nums2):
#     result=[]
#     n=len(nums1)
#     m=len(nums2)
#     i,j=0,0
#     while i>=0 and j >=0 and i<n and j<m:
#         if nums1[i]<=nums2[j]:
#             result.append(nums1[i])
#             i+=1
#         else:
#             result.append(nums2[j])
#             j+=1
#     while i>=0 and i<n-1:
#         result.append(nums1[i])
#         i+=1
#     while j>=0 and j<m-1:
#         result.append(nums[j])
#         j+=1
#     return result


def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high
    while i<=j:
        while pivot>=nums[i] and i<=high-1  :
            i+=1
        while pivot<nums[j] and j>=low+1:
            j-=1
        nums[i],nums[j]=nums[j],nums[i]
    return j
def quick_sort(nums,low,high):
    if low<high:
        p_index=partition(nums,0,len(nums))
        quick_sort(nums,low,p_index-1)
        quick_sort(nums,p_index+1,high)

