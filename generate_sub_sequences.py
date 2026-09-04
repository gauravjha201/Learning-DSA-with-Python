
def solve(nums,i,result,subset):
    if i>=len(nums):
        result.append(subset.copy())
        return 
    subset.append(nums[i])
    solve(nums,i+1,result,subset)
    subset.pop()
    solve(nums,i+1,result,subset)
    




nums=[5,9,7]
result=[]
solve(nums,0,result,[])
print(result)