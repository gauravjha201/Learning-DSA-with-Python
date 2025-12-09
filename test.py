#count number of subset of sum of target
nums=[5,9,4,1]
target=9
def backtrack(index,total):
    if total==target:
        return 1
    if total>target : 
        return 0
    if index>=len(nums):
        return 0
    sum=total+nums[index]
    pick=backtrack(index+1,sum)
    sum=total
    non_pick=backtrack(index+1,sum)
    return pick+non_pick

print(backtrack(0,0))


