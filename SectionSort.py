nums=[6,5,4,3,2,1]
def selection_sort():
    for i in range(0,len(nums)):
        min_ind=i
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j] :
                min_ind=j
        nums[i],nums[min_ind]=nums[min_ind],nums[i]
            
             
selection_sort()
print(nums)


# nums=[4,2,3,7,5,6]
# n=len(nums)
# def selection():
#   for i in range(n):
#       for j in range(i+1,n):
#           if nums[i]>nums[j] :
#               nums[i],nums[j]=nums[j],nums[i]
          
# selection()
# print(nums)

            
