words=["best","great"]

with open("file4.txt","r") as f:
    content=f.read()

for word in words :
    content=content.replace(word,"#"*len(word))

with open("file4.txt","w") as f:
   f.write(content) 