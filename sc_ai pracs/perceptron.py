def mult(weight, x):
    sum = 0
    for i in range(len(weight)):
        sum += weight[i] * x[i]
    return sum
N = int(input("Enter number of inputs: "))
c = float(input("Enter learning constant: "))
desired_op=[]
input_x =  []
for i in range (N):
    temp = list(map(float,input("Enter x vector:").split(",")))
    input_x.append(temp)
    t = float(input("Enter desired output:"))
    desired_op.append(t)
weight = list(map(float,input("Enter weights:").split(",")))
print("Input vectors:",input_x)
print("Desired outputs:",desired_op)
print("Learning rate:",c)
iterate = int(input("Enter number of iterations:"))
for i in range(iterate):
    print("Iteration Number:",i)
    for j in range(N):
        print("Input number:",j)
        net = mult(weight,input_x[j])
        print("Net[",j,"]=",net)
        if (net <=0):
            o = 0
        else:
            o = 1.0
        print("Actual Output:",o)
        delta =list(c*(desired_op[j] - o) * k for k in input_x[j])
        print("delta_w =",delta)
        for m in range(len(weight)):
            weight[m] += delta[m]
        print("Updated weights:: ",weight)

"""
OUTPUT
Enter number of inputs: 3
Enter learning constant: 1
Enter x vector:1,2
Enter desired output:1
Enter x vector:-1,2
Enter desired output:0
Enter x vector:0,-1
Enter desired output:0
Enter weights:1,-0.8
Input vectors: [[1.0, 2.0], [-1.0, 2.0], [0.0, -1.0]]
Desired outputs: [1.0, 0.0, 0.0]
Learning rate: 1.0
Enter number of iterations:3
Iteration Number: 0
Input number: 0
Net[ 0 ]= -0.6000000000000001
Actual Output: 0
delta_w = [1.0, 2.0]
Updated weights::  [2.0, 1.2]
Input number: 1
Net[ 1 ]= 0.3999999999999999
Actual Output: 1.0
delta_w = [1.0, -2.0]
Updated weights::  [3.0, -0.8]
Input number: 2
Net[ 2 ]= 0.8
Actual Output: 1.0
delta_w = [-0.0, 1.0]
Updated weights::  [3.0, 0.19999999999999996]
Iteration Number: 1
Input number: 0
Net[ 0 ]= 3.4
Actual Output: 1.0
delta_w = [0.0, 0.0]
Updated weights::  [3.0, 0.19999999999999996]
Input number: 1
Net[ 1 ]= -2.6
Actual Output: 0
delta_w = [-0.0, 0.0]
Updated weights::  [3.0, 0.19999999999999996]
Input number: 2
Net[ 2 ]= -0.19999999999999996
Actual Output: 0
delta_w = [0.0, -0.0]
Updated weights::  [3.0, 0.19999999999999996]
Iteration Number: 2
Input number: 0
Net[ 0 ]= 3.4
Actual Output: 1.0
delta_w = [0.0, 0.0]
Updated weights::  [3.0, 0.19999999999999996]
Input number: 1
Net[ 1 ]= -2.6
Actual Output: 0
delta_w = [-0.0, 0.0]
Updated weights::  [3.0, 0.19999999999999996]
Input number: 2
Net[ 2 ]= -0.19999999999999996
Actual Output: 0
delta_w = [0.0, -0.0]
Updated weights::  [3.0, 0.19999999999999996]

"""