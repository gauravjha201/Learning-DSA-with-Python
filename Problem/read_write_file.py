# f=open("C:\\Users\\jhaga\\OneDrive\\Desktop\\data\\funny.txt","r")
# f_out=open("C:\\Users\\jhaga\\OneDrive\\Desktop\\data\\funny_wc.txt","w")

# # f.write(" Iam the Best")
# # f.close()

# # print(f.read())
# # f.close()

# for line in f :
#     tokens=line.split(' ')
#     f_out.write("wordcount:"+str(len(tokens))+line)

#     # print(str(tokens)) # this is used to print every word
#     # print(len(tokens))# this is used to count the words

# f.close()
# f_out.close()


# with open("C:\\Users\\jhaga\\OneDrive\\Desktop\\data\\funny.txt","r") as f :#in with statement you don't do file closeing statement
#     print(f.read())

# print(f.closed)

with open("C:\\Users\\jhaga\\OneDrive\\Desktop\\data\\input.txt","w") as f :
    f.write("6,8\n 2,7\n 8,3\n 8,1")
    
