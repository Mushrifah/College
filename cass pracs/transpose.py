import numpy as np
#R=int(input("Number of rows"))
#C=int(input("Number of columns"))
inp=input("Enter string")

inp_list=list(inp)
if(len(inp_list)<5*5):
    while (len(inp_list)!=5*5):
        inp_list.append("x")

matrix=np.array(inp_list).reshape(5,5)
print(matrix)
t= np.transpose(matrix)
print(t)
transpose_list=t.tolist()
result=sum(transpose_list,[])
print("".join(result))

#decrypt
de_msg=np.transpose(t)
de_msglist=de_msg.tolist()
print(de_msglist)
initial=sum(de_msglist,[])
print("".join(initial))
