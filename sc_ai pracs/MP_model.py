#Step 1

x1=[0,0,1,1]

x2=[0,1,0,1]

r1=[]

for i in range(len(x1)):

if(x1[i] and x2[i]== True):

r1.append(1)

else:

r1.append(0)

print(r1)


#Step 2

for i in range(len(x1)):

if(r1[i]==0):

if(x1[i]==0 and x2[i]==0):

print("0<Theta")

elif(x1[i]==0 and x2[i]==1):

print("w2<theta")

elif(x1[i]==1 and x2[i]==0):

print("w1<theta")

elif(r1[i]==1): 

		print("w1+w2>=Theta")

theta = int(input(" Enter Theta "))

w1 = int(input(" Enter w1 "))

w2 = int(input(" Enter w2 "))	


count=0

for i in range(len(x1)):

if(r1[i]==0): 

		if(x1[i]==0 and x2[i]==0):

			if(0<theta):

				print("true");count+=1

			else:

				print("False")

		elif(x1[i]==0 and x2[i]==1):

if(w2<theta):

				print("true");count+=1

			else:

				print("False")

		elif(x1[i]==1 and x2[i]==0):

			if(w1<theta):

				print("True");count+=1

			else:

				print("False")


	elif(r1[i]==1):

		#x1w1+x2w2>=o

		if(w1+w2>=theta):

			print("true");count+=1

		else:

				print("False")

if(count==4):

	print("The conditions are satisfied")

