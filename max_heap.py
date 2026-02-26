nums=[10,7,6,4,5,4,5,5,3,2]

def heapify(nums,ind,val):
    if nums[ind]>val:
        nums[ind]=val
        heapify_down(nums,ind)
    else:
        nums[ind]=val
        heapify_up(nums,ind)
    
    return nums

heapify(nums,1,12)
print(nums)

def heapify_down(nums,ind):
    n=len(nums)

    large_ind=ind
    left_ind=2*ind+1
    right_ind=2*ind+2

    if left_ind<n and nums[left_ind]>nums[large_ind]:
        large_ind=left_ind
    if right_ind<n and nums[right_ind]>nums[large_ind]:
        large_ind=right_ind
    
    if large_ind!=ind:
        nums[large_ind],nums[ind]=nums[ind],nums[large_ind]
        heapify_down(nums,large_ind)
    
def heapify_up(nums,ind):
    n=len(nums)
    parent_ind=(ind-1)//2

    if parent_ind>0 and nums[parent_ind]<nums[ind]:
        nums[parent_ind],nums[ind]=nums[ind],nums[parent_ind]
        heapify_up(nums,parent_ind)



    