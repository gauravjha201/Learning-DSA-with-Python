
def solve(nums,i,total,k):
  if total==k:
    return 1
  if total>k or i>=len(nums):
    return 0
  sums=total+nums[i]
  pick=solve(nums,i+1,sums,k)
  sums=total
  not_pick=solve(nums,i+1,sums,k)
  return pick+not_pick
  

nums=[1,3,2,1]
k=3
print(solve(nums,0,0,k))
