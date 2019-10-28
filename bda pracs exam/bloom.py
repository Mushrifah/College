a=[0,0,0,0,0,0,0,0,0,0]
def hash(a):
    h1=(6*a+1)%10
    h2=(2*a+1)%10
    return h1,h2
def hcal(word):
    print([word[i:i+1]for i in range(0,len(word))])
    s=0
    for i in range(len(word)):
        s+=ord(word[i])
    return s

word=input()
s=hcal(word)
s1,s2=hash(s)
print(s1,s2)
a[s1]=a[s2]=1
print(a)

ip=input("enter the word to check whether its spam or not: ")
s=hcal(ip)
s1,s2=hash(s)
print(s1,s2)
if(a[s1]==1 and a[s2]==1):
    print("It is a spam")
else:
    print("Not a spam")


"""
Output:

lol
['l', 'o', 'l']
3 5
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
enter the word to check whether its spam or not: anam
['a', 'n', 'a', 'm']
9 7
Not a spam
"""
