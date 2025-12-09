n=[5,3,3,2,1,5,6,7,7,7,8,10]
m=[10,111,1,9,5,67,2,7]

# this is using hashing
# hash_list=[0]*11
 
# for i in n :
#     hash_list[i]+=1
# for i in m :
#     if i<1 or i>10 :
#         print(0,end=" ")
#     else:
#         print(hash_list[i],end=" ")



# this is using dictionary
freq_dic={}
for i in n:
    if i in freq_dic:
        freq_dic[i] += 1
    else:
        freq_dic[i] = 1

for i in m:
    if i in freq_dic:
        print(freq_dic[i], end=" ")
    else:
        print(0, end=" ")

