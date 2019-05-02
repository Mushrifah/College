import math
car_no=[1,2,3,4,5,6,7,8,9,10]
color=['red','red','red','yellow','yellow','yellow','yellow','yellow','red','red']
typeof=['sports','sports','sports','sports','sports','SUV','SUV','SUV','SUV','sports']
origin=['domestic','domestic','domestic','domestic','imported','imported','imported','domestic','imported','imported']
stolen=['yes','no','yes','no','yes','no','yes','no','no','yes']
p=stolen.count('yes')
n=stolen.count('no')

#probablities of color
print('\nColor')
pi=[0]*2
ni=[0]*2
color_set=list(set(color)) 
for i in range (0,2):
    for j in range (0,len(car_no)):
        if(color_set[i]==color[j]):
            if(stolen[j]=='yes'):
                pi[i]=pi[i]+1
            else:
                ni[i]=ni[i]+1
print(color_set)
print(pi)
print(ni)

#probablities of typeof
print('\nType')
pi1=[0]*2
ni1=[0]*2
typeof_set=list(set(typeof)) 
for i in range (0,2):
    for j in range (0,len(car_no)):
        if(typeof_set[i]==typeof[j]):
            if(stolen[j]=='yes'):
                pi1[i]=pi1[i]+1
            else:
                ni1[i]=ni1[i]+1
print(typeof_set)
print(pi1)
print(ni1)

#probablities of origin
print('\nOrigin')
pi2=[0]*2
ni2=[0]*2
origin_set=list(set(origin)) 
for i in range (0,2):
    for j in range (0,len(car_no)):
        if(origin_set[i]==origin[j]):
            if(stolen[j]=='yes'):
                pi2[i]=pi2[i]+1
            else:
                ni2[i]=ni2[i]+1
print(origin_set)
print(pi2)
print(ni2)
a=[0]*3
print("Enter the sample:")
a[0]=str(input("Color="))
a[1]=str(input("Type="))
a[2]=str(input("Origin="))

#CALCULATING PROBABLITY
#positive
x=[0]*3
for i in range (0,2):
    if(a[0]==color_set[i]):
        x[0]=pi[i]/p
    if(a[1]==typeof_set[i]):/
        x[1]=pi1[i]/p
    if(a[2]==origin_set[i]):
        x[2]=pi2[i]/p
print("P(p)="+str(x[0]*x[1]*x[2]*(p/10)))
#negative
x1=[0]*3
for i in range (0,2):
    if(a[0]==color_set[i]):
        x1[0]=ni[i]/n
    if(a[1]==typeof_set[i]):
        x1[1]=ni1[i]/n
    if(a[2]==origin_set[i]):
        x1[2]=ni2[i]/n
print("P(n)="+str(x1[0]*x1[1]*x1[2]*(n/10)))
