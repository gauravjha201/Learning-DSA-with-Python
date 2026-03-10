nums=[4,6,3,7,4,8,3,8,4]
n=len(nums)
def heapify_down(nums,n,ind):
    large_ind=ind
    L_ind=ind*2+1
    R_ind=ind*2+2
    if L_ind<n and nums[L_ind]>nums[large_ind]:
        large_ind=L_ind

    if R_ind<n and nums[R_ind]>nums[large_ind]:
        large_ind=R_ind

    if large_ind!=ind:
        nums[ind],nums[large_ind]=nums[large_ind],nums[ind]
        heapify_down(nums,n,large_ind)
    
def heap_sort(nums):
    n=len(nums)
    for i in range((n//2)-1,-1,-1):
        heapify_down(nums,n,i)

    for last_ind in range(n-1,0,-1):
        nums[0],nums[last_ind]=nums[last_ind],nums[0]
        heapify_down(nums,last_ind,0) 
    
    return nums

print(heap_sort(nums))
