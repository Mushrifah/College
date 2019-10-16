import numpy as np
def mult(weight, x):
    sum = 0
    for i in range(len(weight)):
        sum += weight[i] * x[i]
    return sum
N = int(input("Enter number of inputs: "))
c = float(input("Enter learning constant: "))
l = float(input("Enter lambda value: "))
input_x = [[1.0, -2.0, 1.5, 0.0], [1.0, -0.5, -2.0, -1.5], [0.0, 1.0, -1.0, 1.5]]
weight = [1.0, -1.0, 0.0, 0.5]
# for i in range (N):
#     temp = list(map(float,input("Enter x vector:").split(",")))
#     input_x.append(temp)
# weight = list(map(float,input("Enter weights:").split(",")))
print("Input vectors:",input_x)
print("Learning rate:",c)
print("Lambda:",l)
mode = int(input("Enter 1 for bipolar continuous and 0 for bipolar binary"))
iterate = int(input("Enter number of iterations:"))
for i in range(iterate):
    print("Iteration Number:",i)
    for j in range(N):
        o=1
        print("Input number:",j)
        net = mult(weight,input_x[j])
        print("Net[",j,"]=",net)
        if (net <=0):
            o = -1.0
        print("Actual Output:",o)
        if(mode == 1):
            o = np.tanh(l*net/2)
            print("tanh is:",o)
        delta = list(c * o * k for k in input_x[j])
        print("delta_w =", delta)
        for m in range(len(weight)):
            weight[m] += delta[m]
        print("Updated weights:: ", weight)

"""

OUTPUT:
Enter number of inputs: 3
Enter learning constant: 1
Enter lambda value: 1
Input vectors: [[1.0, -2.0, 1.5, 0.0], [1.0, -0.5, -2.0, -1.5], [0.0, 1.0, -1.0, 1.5]]
Learning rate: 1.0
Lambda: 1.0
Enter 1 for bipolar continuous and 0 for bipolar binary0
Enter number of iterations:3
Iteration Number: 0
Input number: 0
Net[ 0 ]= 3.0
Actual Output: 1
delta_w = [1.0, -2.0, 1.5, 0.0]
Updated weights::  [2.0, -3.0, 1.5, 0.5]
Input number: 1
Net[ 1 ]= -0.25
Actual Output: -1.0
delta_w = [-1.0, 0.5, 2.0, 1.5]
Updated weights::  [1.0, -2.5, 3.5, 2.0]
Input number: 2
Net[ 2 ]= -3.0
Actual Output: -1.0
delta_w = [-0.0, -1.0, 1.0, -1.5]
Updated weights::  [1.0, -3.5, 4.5, 0.5]
Iteration Number: 1
Input number: 0
Net[ 0 ]= 14.75
Actual Output: 1
delta_w = [1.0, -2.0, 1.5, 0.0]
Updated weights::  [2.0, -5.5, 6.0, 0.5]
Input number: 1
Net[ 1 ]= -8.0
Actual Output: -1.0
delta_w = [-1.0, 0.5, 2.0, 1.5]
Updated weights::  [1.0, -5.0, 8.0, 2.0]
Input number: 2
Net[ 2 ]= -10.0
Actual Output: -1.0
delta_w = [-0.0, -1.0, 1.0, -1.5]
Updated weights::  [1.0, -6.0, 9.0, 0.5]
Iteration Number: 2
Input number: 0
Net[ 0 ]= 26.5
Actual Output: 1
delta_w = [1.0, -2.0, 1.5, 0.0]
Updated weights::  [2.0, -8.0, 10.5, 0.5]
Input number: 1
Net[ 1 ]= -15.75
Actual Output: -1.0
delta_w = [-1.0, 0.5, 2.0, 1.5]
Updated weights::  [1.0, -7.5, 12.5, 2.0]
Input number: 2
Net[ 2 ]= -17.0
Actual Output: -1.0
delta_w = [-0.0, -1.0, 1.0, -1.5]
Updated weights::  [1.0, -8.5, 13.5, 0.5]

Enter number of inputs: 3
Enter learning constant: 1
Enter lambda value: 1
Input vectors: [[1.0, -2.0, 1.5, 0.0], [1.0, -0.5, -2.0, -1.5], [0.0, 1.0, -1.0, 1.5]]
Learning rate: 1.0
Lambda: 1.0
Enter 1 for bipolar continuous and 0 for bipolar binary 1
Enter number of iterations:3
Iteration Number: 0
Input number: 0
Net[ 0 ]= 3.0
Actual Output: 1
tanh is: 0.9051482536448664
delta_w = [0.9051482536448664, -1.8102965072897328, 1.3577223804672995, 0.0]
Updated weights::  [1.9051482536448665, -2.810296507289733, 1.3577223804672995, 0.5]
Input number: 1
Net[ 1 ]= -0.15514825364486606
Actual Output: -1.0
tanh is: -0.07741889336533958
delta_w = [-0.07741889336533958, 0.03870944668266979, 0.15483778673067916, 0.11612834004800937]
Updated weights::  [1.8277293602795268, -2.771587060607063, 1.5125601671979787, 0.6161283400480093]
Input number: 2
Net[ 2 ]= -3.3599547177330273
Actual Output: -1.0
tanh is: -0.9328586152504333
delta_w = [-0.0, -0.9328586152504333, 0.9328586152504333, -1.39928792287565]
Updated weights::  [1.8277293602795268, -3.7044456758574964, 2.445418782448412, -0.7831595828276408]
Iteration Number: 1
Input number: 0
Net[ 0 ]= 12.904748885667136
Actual Output: 1
tanh is: 0.9999950275813748
delta_w = [0.9999950275813748, -1.9999900551627496, 1.4999925413720623, 0.0]
Updated weights::  [2.8277243878609015, -5.704435731020246, 3.9454113238204744, -0.7831595828276408]
Input number: 1
Net[ 1 ]= -1.0361410200284635
Actual Output: -1.0
tanh is: -0.4762094545678828
delta_w = [-0.4762094545678828, 0.2381047272839414, 0.9524189091357655, 0.7143141818518242]
Updated weights::  [2.3515149332930187, -5.466331003736305, 4.89783023295624, -0.0688454009758166]
Input number: 2
Net[ 2 ]= -10.46742933815627
Actual Output: -1.0
tanh is: -0.9999431054273442
delta_w = [-0.0, -0.9999431054273442, 0.9999431054273442, -1.4999146581410163]
Updated weights::  [2.3515149332930187, -6.466274109163649, 5.897773338383584, -1.568760059116833]
Iteration Number: 2
Input number: 0
Net[ 0 ]= 24.130723159195693
Actual Output: 1
tanh is: 0.9999999999337493
delta_w = [0.9999999999337493, -1.9999999998674987, 1.499999999900624, 0.0]
Updated weights::  [3.351514933226768, -8.466274109031147, 7.397773338284209, -1.568760059116833]
Input number: 1
Net[ 1 ]= -4.857754600150826
Actual Output: -1.0
tanh is: -0.9845839377693407
delta_w = [-0.9845839377693407, 0.49229196888467036, 1.9691678755386814, 1.4768759066540111]
Updated weights::  [2.3669309954574276, -7.973982140146477, 9.36694121382289, -0.09188415246282178]
Input number: 2
Net[ 2 ]= -17.4787495826636
Actual Output: -1.0
tanh is: -0.9999999487014026
delta_w = [-0.0, -0.9999999487014026, 0.9999999487014026, -1.499999923052104]
Updated weights::  [2.3669309954574276, -8.97398208884788, 10.366941162524293, -1.5918840755149257]
"""