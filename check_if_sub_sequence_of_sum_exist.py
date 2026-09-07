
def solve(nums,i,total,k):
  if total==k:
    return True
  if total>k:
    return False
  if i>=len(nums):
    return False
  total+=nums[i]
  pick=solve(nums,i+1,total,k)
  if pick:return True
  total-=nums[i]
  not_pick=solve(nums,i+1,total,k)
  return not_pick
  
    

nums=[5,1,1,9,2,10]
# nums=[5,7,3]

k=9
print(solve(nums,0,0,k))