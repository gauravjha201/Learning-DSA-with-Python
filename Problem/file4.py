word="best"

with open("file4.txt","r") as f:
    content=f.read()
newcontent=content.replace(word,"great")

with open("file4.txt","w") as f:
    f.write(newcontent)
