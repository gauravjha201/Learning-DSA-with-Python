#this is a sorted array,remove dulicate and return no. of unique element
nums=[1,1,1,2,2,3,4,4,4,5,5,6,7,7]


# freq_dic={}
# for i in range(0,len(freq_dic)):
#     freq_dic[nums[i]]=0
# j=0
# for k in freq_dic :
#     nums[j]=k
#     j+=1
# print(j)

#Approach optimal
def remove():

    n=len(nums)
    if n==1 :
        return 1
    i=0
    j=i+1
    while j<n :
        if nums[i]!=nums[j] :
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
        j+=1

    return i+1

print(remove())






