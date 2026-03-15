nums=[3,2,1,5,6,4]
n=len(nums)

def heapify_down(nums,ind):
    n=len(nums)
    large_ind=ind
    L_ind=ind*2+1
    R_ind=ind*2+2
    if L_ind<n and nums[L_ind]>nums[large_ind]:
        large_ind=L_ind
    if R_ind<n and nums[R_ind]>nums[large_ind]:
        large_ind=R_ind
    if large_ind!=ind:
        nums[ind],nums[large_ind]=nums[large_ind],nums[ind]
        heapify_down(nums,large_ind)

for i in range((n//2)-1,-1,-1):
    heapify_down(nums,i)
print(nums)


