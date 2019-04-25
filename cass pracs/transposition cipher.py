import numpy as np
message = input("Enter Message: ")
message_list=[]
for i in range (len(message)):
        message_list.append(message[i])
matrix = [[]*k for k in range (5)]
k=0
for i in range (5):
    for j in range (5):
        if(k<len(message_list)):
            print(message_list[k])
            matrix[i].append(message_list[k])
            k=k+1
        else:
            matrix[i].append(" ")
print(matrix)
messager=""
transpose= [[]*k for k in range (5)]
for i in range (5):
    for j in range (5):
        transpose[i].append(matrix[j][i])
        messager = messager + matrix[j][i]
print(transpose)
print(messager)
