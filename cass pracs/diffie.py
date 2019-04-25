import random
import math
g=13
p=19
a=random.randrange(2,50)
b=random.randrange(2,50)
print("Alice chose secret random number: ",a)
print("Bob chose secret random number: ",b)
A=pow(g,a,p)
B=pow(g,b,p)
print("Alice computed g^a mod p as: ",A," and later sent it to Bob")
print("Bob computed g^b mod p as: ",B," and later sent it to Alice")
A_bob=pow(A,b,p)
B_alice=pow(B,a,p)
print("Alice got key as: ",B_alice)