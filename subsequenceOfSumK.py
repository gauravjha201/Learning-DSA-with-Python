# nums=[5,7,9,4]#this is optimal approach
# target=9
# result=[]
# subset=[]
# def subSequence(index,total,subset):
#     if total==target :
#         result.append(subset.copy())
#         return
#     if total>target:
#         return 
#     if index>=len(nums):
#         return
#     subset.append(nums[index])
#     total=total+nums[index]
#     subSequence(index+1,total,subset)
#     e=subset.pop()
#     total=total-e
#     subSequence(index+1,total,subset)

#     return result
# print(subSequence(0,0,subset))


# result=[]#this is brute force approach
# subset=[]
# nums=[5,9,4,1]
# def solve(index,target,subset):
#     if index>=len(nums):
#         if sum(subset)==target :
#             result.append(subset.copy())
#         return
#     subset.append(nums[index])
#     solve(index+1,target,subset)
#     subset.pop()
#     solve(index+1,target,subset)
#     return result

# print(solve(0,9,subset))


# #check if subset of sum of target or not
# nums=[5,9,4,1]
# target=9
# subset=[]
# result=[]
# def backtrack(index,total,subset):
#     if total==target:
#         result.append(subset.copy())
#         return True
#     if total>target or index>=len(nums):
#         return False
    
#     subset.append(nums[index])
#     total=total+nums[index]
#     pick=backtrack(index+1,total,subset)
#     if pick==True :
#         return True
#     e=subset.pop()
#     total=total-e
#     not_pick=backtrack(index+1,total,subset)
#     return not_pick

# print(backtrack(0,0,subset))


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






