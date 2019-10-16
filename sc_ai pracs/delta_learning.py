import numpy as np
def mult(weight, x):
    sum = 0
    for i in range(len(weight)):
        sum += weight[i] * x[i]
    return sum
N = int(input("Enter number of inputs: "))
c = float(input("Enter learning constant: "))
input_x = [[1.0, -2.0, 0.0, -1.0], [0.0, 1.5, -0.5, -1.0], [-1.0, 1.0, 0.5, -1.0]]
weight = [1,-1,0,0.5]
desired_op = [-1,-1,1]
# for i in range (N):
#      temp = list(map(float,input("Enter x vector:").split(",")))
#      input_x.append(temp)
#      t = float(input("Enter desired output:"))
#      desired_op.append(t)
#weight = list(map(float,input("Enter weights:").split(",")))
print("Input vectors:",input_x)
print("Learning rate:",c)
mode = int(input("Enter 1 for bipolar continuous and 0 for unipolar continuous "))
iterate = int(input("Enter number of iterations:"))
for i in range(iterate):
    print("Iteration Number:",i)
    for j in range(N):
        o = 1
        print("Input number:",j)
        net = mult(weight,input_x[j])
        print("Net[",j,"]=",net)
        if(mode == 1):
            o = np.around(np.tanh(net / 2),3)
            der = (1 - o * o) / 2
        else:
            o = np.around(1/(1+2.718**(-1*net)),3)
            der = (1 - o ) * o
        print("output is :",o)
        print("f'(net) is :", der)
        r = desired_op[j] - o
        print("Learning signal is: ",r)
        delta = list(c * r * der * k for k in input_x[j])
        print("delta_w =", delta)
        for m in range(len(weight)):
            weight[m] += delta[m]
        print("Updated weights:: ", weight)


#OUTPUT
# Enter number of inputs: 3
# Enter learning constant: 0.1
# Enter x vector:1,-2,0,-1
# Enter desired output:-1
# Enter x vector:0,1.5,-0.5,-1
# Enter desired output:-1
# Enter x vector:-1,1,0.5,-1
# Enter desired output:1
# Enter weights:1,-1,0,0.5
# Input vectors: [[1.0, -2.0, 0.0, -1.0], [0.0, 1.5, -0.5, -1.0], [-1.0, 1.0, 0.5, -1.0]]
# Learning rate: 0.1
# Enter 1 for bipolar continuous and 0 for unipolar continuous 1
# Enter number of iterations:1
# Iteration Number: 0
# Input number: 0
# Net[ 0 ]= 2.5
# output is : 0.848
# f'(net) is : 0.14044800000000002
# Learning signal is:  -1.8479999999999999
# delta_w = [-0.025954790400000004, 0.05190958080000001, -0.0, 0.025954790400000004]
# Updated weights::  [0.9740452096, -0.9480904192, 0.0, 0.5259547904]
# Input number: 1
# Net[ 1 ]= -1.9480904192000001
# output is : -0.75
# f'(net) is : 0.21875
# Learning signal is:  -0.25
# delta_w = [-0.0, -0.008203125, 0.0027343750000000003, 0.0054687500000000005]
# Updated weights::  [0.9740452096, -0.9562935442, 0.0027343750000000003, 0.5314235404000001]
# Input number: 2
# Net[ 2 ]= -2.4603951067
# output is : -0.843
# f'(net) is : 0.1446755
# Learning signal is:  1.843
# delta_w = [-0.026663694650000003, 0.026663694650000003, 0.013331847325000002, -0.026663694650000003]
# Updated weights::  [0.94738151495, -0.92962984955, 0.016066222325, 0.5047598457500001]


# Enter number of inputs: 3
# Enter learning constant: 0.1
# Input vectors: [[1.0, -2.0, 0.0, -1.0], [0.0, 1.5, -0.5, -1.0], [-1.0, 1.0, 0.5, -1.0]]
# Learning rate: 0.1
# Enter 1 for bipolar continuous and 0 for unipolar continuous 0
# Enter number of iterations:1
# Iteration Number: 0
# Input number: 0
# Net[ 0 ]= 2.5
# output is : 0.924
# f'(net) is : 0.07022399999999997
# Learning signal is:  -1.924
# delta_w = [-0.013511097599999996, 0.02702219519999999, -0.0, 0.013511097599999996]
# Updated weights::  [0.9864889024, -0.9729778048, 0.0, 0.5135110976]
# Input number: 1
# Net[ 1 ]= -1.9729778047999997
# output is : 0.122
# f'(net) is : 0.107116
# Learning signal is:  -1.1219999999999999
# delta_w = [-0.0, -0.0180276228, 0.0060092076, 0.0120184152]
# Updated weights::  [0.9864889024, -0.9910054276, 0.0060092076, 0.5255295128]
# Input number: 2
# Net[ 2 ]= -2.500019239
# output is : 0.076
# f'(net) is : 0.070224
# Learning signal is:  0.924
# delta_w = [-0.0064886976, 0.0064886976, 0.0032443488, -0.0064886976]
# Updated weights::  [0.9800002047999999, -0.98451673, 0.0092535564, 0.5190408152]
