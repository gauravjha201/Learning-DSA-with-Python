nums=[2,3,5,4,5,4,6,7,10]


def heapify_up(nums,ind):
    n=len(nums)
    parent_ind=(ind-1)//2
    mini=ind

    if mini>0 and nums[mini]<nums[parent_ind]:
        nums[mini],nums[ind]=nums[ind],nums[mini]
        heapify_up(nums,parent_ind)


def heapify_down(nums,ind):
    n=len(nums)
    left_ind=2*ind+1
    right_ind=2*ind+2
    mini=ind
    if mini<n and nums[mini]>nums[left_ind]:
        mini=left_ind
    if mini<n and nums[mini]>nums[right_ind]:
        mini=right_ind
    if mini!=ind:
        nums[ind],nums[mini]=nums[mini],nums[ind]
        heapify_down(nums,mini)


def heapify(nums,val,ind):
    if nums[ind]>val:
        nums[ind]=val
        heapify_up(nums,ind)
    else:
        nums[ind]=val
        heapify_down(nums,ind)

    return nums

heapify(nums,7,1)
print(nums)


    

