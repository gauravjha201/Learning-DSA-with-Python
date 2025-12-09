nums=[1,1,2,3,22,3,3,4,5,6,6]

freq_map={}
for i in range(len(nums)):
    if nums[i] in freq_map :
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1
print (freq_map)





# hash_map={}
# for i in range(len(nums)):
#     hash_map(nums[i])=hash_map.get(nums[i],0)+1

# print (hash_map)
