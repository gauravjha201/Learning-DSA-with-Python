nums=[9,1,5,2,6,8]
n=len(nums)

for ind in range((n//2)-1,-1,-1):
    L_ind=ind*2+1
    R_ind=ind*2+2
    if L_ind<n and nums[L_ind]<nums[ind]:
        print("False")
        break
    if R_ind<n and nums[R_ind]<nums[ind]:
        print("False")
        break
print("True")
    