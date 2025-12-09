
# arr=[0, 1, 1, 1, 1, 0, 0, 0, 1]
# def longestsubarraywithequalzerosones(arr):
#     n = len(arr)
#     result = 0
#     zeros, ones = 0, 0
#     maxlen = 0

#     for i in range(n):
#         if arr[i] == 0:
#             zeros += 1
#         else:
#             ones += 1

#         if zeros==ones:
#             maxlen=i+1
#         elif zeros>ones:
#             ones=0
#             zeros=zeros-ones-1
#         else:
#             zeros=0
#             ones=ones-zeros-1

#     return maxlen   

arr=[0, 1, 1, 1, 1, 0, 0, 1, 1]
count1=0
count0=0
largest_subarray=[]

for i in range(len(arr)):
    count1=0
    count0=0
    subarray=[]
    for j in range(i):
        if (arr[j]==0):
            count0+=1
        else:
            count1+=1
        subarray.append(arr[j])

    if(count0==count1):
        if(len(largest_subarray)<len(subarray)):
            largest_subarray=subarray
print ( largest_subarray)