text="ababcdabababababcbad"#this is not complete now 
pattern="babab"
n=len(text)
m=len(pattern)

def string_matching(text,pattern):
    comparision=0
    occerence=[]
    shift=0
    for i in range(shift,n-m+1):
        match=True
        for j in range(m):
            comparision+=1
            if text[i]!=pattern[j]:
                shift+=1
                break
                
                
        if match==True:
            occerence.append(i)
    return comparision,occerence
print(string_matching(text,pattern))


            




