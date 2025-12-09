
arr=[1,2,3,4,5,6,7,8]
def reverseArray(arr,left,right):
    if left == right or left>right : 
        return 
    arr[left],arr[right]=arr[right],arr[left]
    return reverseArray(arr,left+1,right-1)


reverseArray(arr,0,len(arr)-1)
print(arr)
    

