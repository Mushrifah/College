import numpy as np
print("Enter matrix 1")
a = np.matrix('0 0 1;0 0 1;0 0 0 ')
A= np.array(a)
print(A)

at=A.transpose()
print(at)

u = np.array([1 ,1 ,1])
print("u=\n",u)

v=np.matmul(at, u)
print("v=\n",v)

u=np.matmul(A, v)
print("u=\n",u)


for i in range(3):
  if(u[i] > v[i]):
    print("hub is",i+1)
  elif(u[i] < v[i]):
    print("most authorative",i+1)
