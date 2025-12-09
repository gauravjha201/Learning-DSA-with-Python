nums=[4,2,2,8,3,3,1]
def counting_sort(nums):
    max_num=max(nums)
    count=[0]*(max_num+1)

    print(count)
    for num in nums :
        count[num]+=1
    print(count)

    sortednums=[0]*len(nums)
    k=0
    for i in range(0,len(count)):
        if count[i]>0 :
            for _ in range(0,count[i]):
                sortednums[k]=i
                k+=1
    return sortednums
            
print(f"Sorted Array :{counting_sort(nums)}")

