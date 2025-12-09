def substring(str,i=0):
    #base condition
    if(i==len(str)):
        print("".join(str)) 
    for j in range(i,len(str)):
        word=[c for c in str] #here we intial word length
        word[i],word[j]=word[j],word[i]

        substring(word,i+1)

print(substring("abc"))



