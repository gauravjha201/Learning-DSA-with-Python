s="cadbzabcd"

#brute: TC O(n^2)
def solve(s):
    n=len(s)
    maxi=float("-inf")
    for i in range(n):
        hash_set=set()
        for j in range(i,n):
            if s[j] in hash_set:
                break
            else:
                hash_set.add(s[j])
                maxi=max(maxi,j-i+1)
    return maxi

#optimal: TC:O(n)
def solve(s):
    n=len(s)
    


print(solve(s))


