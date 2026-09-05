def solve(nums,i,result,subset,target):
  if sum(subset)==target:
    result.append(subset.copy())
    return
  if i>=len(nums) or sum(subset)>target:
    return 
  subset.append(nums[i])
  solve(nums,i+1,result,subset,target)
  subset.pop()
  solve(nums,i+1,result,subset,target)

nums=[5,9,3,4,1]
# nums=[5,9,4]
result=[]
target=9
solve(nums,0,result,[],target)
print(result)
