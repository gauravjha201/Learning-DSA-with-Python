
def sprial(mat):
    n=len(mat)
    result=[]
    if n==0:
        return []
    top,left=0,0
    bottam,right=n-1,n-1

    while top<=bottam and left<=right:

        for i in range(left,right+1):
            result.append(mat[top][i])
        top+=1

        for i in range(top,bottam+1):
            result.append(mat[i][right])
        right-=1

        if top<=bottam:
            for i in range(right,left-1,-1):
                result.append(mat[bottam][i])
            bottam-=1

        if left<=right:
            for i in range(bottam,top-1,-1):
                result.append(mat[i][left])
            left+=1
    
    return result

mat=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

print(sprial(mat))