x=int(input('Enter value of dirt'))
y=int(input('Enter value of grease'))
sd=0
if(x>=0 and x<=50):
    sd=(50-x)/50
md=0
if(x>=0 and x<=50):
    md=x/50
if(x>=50 and x<=100):
    md=(100-x)/50
ld=0
if(x>=50 and x<=100):
    ld=(x-50)/50
ng=0
if(y>=0 and y<=50):
    ng=(50-y)/50
mg=0
if(y>=0 and y<=50):
    mg=y/50
if(y>=50 and y<=100):
    mg=(100-y)/50
lg=0
if(y>=50 and y<=100):
    lg=(y-50)/50
r1=min(sd,ng)
r2=min(sd,mg)
r3=min(sd,lg)
r4=min(md,ng)
r5=min(md,mg)
r6=min(md,lg)
r7=min(ld,ng)
r8=min(ld,mg)
r9=min(ld,lg)
out1=max(max(max(r1,r2),r3),max(r4,r5))
out2=max(max(max(r6,r7),r8),r9)
out=max(out1,out2)
if(r1==out):
    vs=out
    z=10-10*vs
if(r4==out):
    s=out
    z1=10*s
    z2=25-15*s
    z=(z1+z2)/2
if(r2==out or r5==out or r7==out):
    m=out;z1=15*m+10
    z2=40-15*m
    z=(z1+z2)/2
if(r3==out or r6==out or r8==out):
    l=out;z1=15*l+25
    z2=60-20*l
    z=(z1+z2)/2
if(r9==out):
    vl=out
    z=40+20*vl
print('value of washtime is')
print(z)

'''
C:\Users\FY-COMP32\Downloads>python p1.py
Enter value of dirt80
Enter value of grease90
value of washtime is
52.0

C:\Users\FY-COMP32\Downloads>python p1.py
Enter value of dirt60
Enter value of grease70
value of washtime is
25.0

C:\Users\FY-COMP32\Downloads>python p1.py
Enter value of dirt10
Enter value of grease20
value of washtime is
4.0
'''