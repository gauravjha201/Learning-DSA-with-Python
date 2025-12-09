def insertionsort(nums):
    for i in range(1,len(nums)-1):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key :
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key

def bucketsort(nums):
    bucket_num=len(nums)   
    max_val=max(nums)     
    buckets=[[] for _ in nums] #create bucket

    for num in nums:# insert number in bucket by index
        index=int(num*bucket_num/(max_val+1))
        buckets[index].append(num)
    
    # for num in nums :# this insert only for fractional values
    #     index=int(bucket_num*num)
    #     buckets[index].append(num)

    for bucket in buckets:#sort every bucket
        insertionsort(bucket)
    
    sorted_nums=[]

    for bucket in buckets:# merge all bucket
        sorted_nums.extend(bucket)
    
    return sorted_nums

# nums=[0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
nums=[29, 25, 3, 49, 9, 37, 21, 43]
print(bucketsort(nums))


