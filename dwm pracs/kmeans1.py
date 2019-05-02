# implementation of k mean clustering
import time
import sys
a=[]
c1=[]
c2=[]
c3=[]
co1=0
co2=0
co3=0
n=int(input("Enter the number of data elements\n")) 
if(n<=3):
  print("Invalid number of data")
  sys.exit()
for i in range(n):
  d=int(input("Enter the data: "))
  a.append(d)
print("This is your data: ",a)
print("A cluster of size 3 is preparing...")
time.sleep(5)
#print(m1,m2,m3)
m1=a[0]
m2=a[1]
m3=a[2]
k=0
l=len(a)
l=l
for i in range(l):
  if(abs(a[i]-m1)<abs(a[i]-m2)):
    if(abs(a[i]-m1)<abs(a[i]-m3)):
      c1.append(a[i])
      k=k+1
    else:
      c3.append(a[i])
      k=k+1
  elif(abs(a[i]-m2)<abs(a[i]-m1)):
    if(abs(a[i]-m2)<abs(a[i]-m3)):
      c2.append(a[i])
      k=k+1
    else:
      c3.append(a[i])
      k=k+1
  elif(abs(a[i]-m3)<abs(a[i]-m1)):
    if(abs(a[i]-m3)<abs(a[i]-m2)):
      c3.append(a[i])
      k=k+1
    else:
      c2.append(a[i])
      k=k+1
print("cluster1:",c1,"\tmean1",m1)
print("cluster2:",c2,"\tmean2",m2)
print("cluster3:",c3,"\tmean3",m3) 
f=0
while(f!=1):
  co1=0
  co2=0
  co3=0 
  m1=(sum(c1)/len(c1))
  m2=(sum(c2)/len(c2))
  m3=(sum(c3)/len(c3))
  dc1=list(c1)
  dc2=list(c2)
  dc3=list(c3)
  c1=[]
  c2=[]
  c3=[]
  for i in range(l):
    if(abs(a[i]-m1)<abs(a[i]-m2)):
      if(abs(a[i]-m1)<abs(a[i]-m3)):
        c1.append(a[i])
        k=k+1
      else:
        c3.append(a[i])
        k=k+1
    elif(abs(a[i]-m2)<abs(a[i]-m1)):
      if(abs(a[i]-m2)<abs(a[i]-m3)):
        c2.append(a[i])
        k=k+1
      else:
        c3.append(a[i])
        k=k+1
    elif(abs(a[i]-m3)<abs(a[i]-m1)):
      if(abs(a[i]-m3)<abs(a[i]-m2)):
        c3.append(a[i])
        k=k+1
      else:
        c2.append(a[i])
        k=k+1
  if(set(dc1)==set(c1)):
    co1=1
  if(set(dc2)==set(c2)):
    co2=1
  if(set(dc3)==set(c3)):
    co3=1
  if(co1+co2+co3==3):
    f=1
print("cluster1:",c1,"\tmean1",m1)   
print("cluster2:",c2,"\tmean2",m2)
print("cluster3:",c3,"\tmean3",m3)


 
