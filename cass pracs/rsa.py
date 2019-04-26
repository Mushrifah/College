import  random
def isPrime(n):
    for i in range(2,sqrt(n)):
        if(n%i==0):
            return (False)
    return (True)
prime = []
for i in range (3,100):
    if(isPrime(i)):
        prime.append(i)
p=random.choice(prime)
q=0
while(1):
    q=random.choice(prime)
    if(q!=p):
        break
print("p= ",p)
print("q= ",q)
n=p*q
phi=(p-1)*(q-1)
print("n= ",n)
print("phi(n)= ",phi)
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
E=[]
for i in range(2,phi):
    if(gcd(i,phi)==1):
        E.append(i)
e=random.choice(E)
print("e= ",e)
x= e%phi
d=0
for i in range (1,phi):
    if((x*i)%phi==1):
        d=i
        break
print("d= ",d)
print((e*d)%phi)

print("Private Key: {",d,p,q,"}")
print("Public Key: {",e,n,"}")

message=str(input("Enter the message: "))
mlist=[]
for i in range(len(message)):
    mlist.append(ord(message[i]))
print(mlist)
c=[]
k=0
def encrypt(mlist):
    for i in range(len(message)):
        k=0
        k=pow(mlist[i],e)%n
        c.append(k)
encrypt(mlist)
m=[]
print("cryptic= ",c)
def decrypt(c):
    for i in range(len(message)):
        k=0
        k=pow(c[i],d)%n
        m.append(k)
decrypt(c)
print("message= ",m)
