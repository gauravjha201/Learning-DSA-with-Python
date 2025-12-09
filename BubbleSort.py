# nums=[2,4,3,1,9,5,6]
# n=len(nums)
# def Bubble_sort():
#     for i in range(n-2,-1,-1):
#         is_swap=False
#         for j in range(0,i+1):
#             if nums[j]>nums[j+1] :
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#                 is_swap=True
#         if is_swap==False :
#             return

# Bubble_sort()
# print(nums)


# nums=[4,3,1,5,2]
# n=len(nums)
# def bubble():
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if nums[j]>nums[j+1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]

# bubble()
# print(nums)

def bubbleSort(self,arr):
    n=len(arr)
    for i in range(n):
        j=i+1
        for j in range(n):
            if arr[i]<arr[j]:
                arr[i]=arr[i]+arr[j]
                arr[j]=arr[i]-arr[j]
                arr[i]=arr[i]-arr[j]
arr=[4,3,1,9,7]
bubbleSort(arr)
print(arr)


            
                
 