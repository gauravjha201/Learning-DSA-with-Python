nums=[3,2,1,5,6,4]
n=len(nums)



def heapify_down(nums,ind):
    n=len(nums)
    small_ind=ind
    L_ind=ind*2+1
    R_ind=ind*2+2
    if L_ind<n and nums[L_ind]<nums[small_ind]:
        small_ind=L_ind
    if R_ind<n and nums[R_ind]<nums[small_ind]:
        small_ind=R_ind
    if small_ind!=ind:
        nums[ind],nums[small_ind]=nums[small_ind],nums[ind]
        heapify_down(nums,small_ind)

for i in range((n//2)-1,-1,-1):
    heapify_down(nums,i)

print(nums)    

