import sympy 
import random
def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
p=sympy.randprime(1,50)
q=sympy.randprime(1,50)
print("Randomly Generated Prime Numbers are: ",p," and ",q)
N=p*q
print("Value of N: ",N)
phi=(p-1)*(q-1)
print("Totient of N: ",phi)
#e=sympy.randprime(1,50)
e=random.randint(1,50)
print("Encryption Component is: ",e)
if e>1 and e<phi and gcd(e,phi) == 1:
    print("e and Totient of N are Co-primes")
else:
    print("e and Totient of N are not Co-primes")
