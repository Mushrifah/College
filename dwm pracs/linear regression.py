print("Enter the number of values:")
n=int(input())
print("Enter the values of x")
x=[]
y=[]
for i in range (0,n):
    x.append(int(input()))
print("Enter the values of y")
for i in range (0,n):
    y.append(int(input()))
#calculating x_mean & y_mean
x_mean=0
y_mean=0
for i in range (0,n):
    x_mean=x_mean + x[i]
    y_mean=y_mean + y[i]
x_mean = x_mean/n
y_mean = y_mean/n
#calculating b1
b1_num=0
b1_denom=0
for i in range (0,n):
    b1_num=b1_num + ((x[i]-x_mean)*(y[i]-y_mean))
    b1_denom= b1_denom + (x[i]-x_mean)*(x[i]-x_mean)
b1=0
b1=b1_num/b1_denom
print("b1=")
print(b1)
#calculating b0
b0=0
b0= y_mean - b1*x_mean
print("b0=")
print(b0)
#finding the value of y for some x
print("Enter x")
x_n=int(input())
y_n=0
y_n=b0+b1*x_n
print("y=")
print(y_n)
