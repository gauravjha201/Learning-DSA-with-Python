st="abc"
ans=""
def permutation(st,ans):
    if len(st)==0:
        print(ans)
        return 


    for i in range(len(st)):

        ch=st[i]
        left=st[0:i]
        right=st[i+1:]
        permutation(left+right,ans+ch)

permutation(st,ans)



