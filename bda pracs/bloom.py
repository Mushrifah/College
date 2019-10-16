def hash1(x, hashArr):
    h1 = (6*x +1)%6
    print(x,h1)
    if hashArr[h1] == 0:
        hashArr[h1] = 1
    return


def hash2(x, hashArr):
    h2 = (2*x +1)%6
    print(x,h2)
    if hashArr[h2] == 0:
        hashArr[h2] = 1
    return


def checkHash1(x, hashArr):
    h1 = (6*x +1)%6
    if hashArr[h1] == 1:
        return 1
    else:
        return 0


def checkHash2(x, hashArr):
    h2 = (2*x +1)%6
    if hashArr[h2] == 1:
        return 1
    else:
        return 0
       

arr = [0] * 6
em= ["cat", "rat", "dog"]

for e in em:
    email = list(e)
    sumE = 0
    for i in email:
        sumE += ord(i)
    print(sumE)
    hash1(sumE, arr)
    hash2(sumE, arr)
    print(arr)
 
inp = ""
while True:
    inp = input("Enter q to Exit or Enter the email: ")
    if inp == "q":
        break
    else:
        inp = list(inp)
        sumInp = 0
        for i in inp:
            sumInp += ord(i)
        chk = 0
        chk += checkHash1(sumInp, arr)
        chk += checkHash2(sumInp, arr)
        if chk == 2:
            print("Spam eMail ID!!")
        else:
            print("Congratulations!!")

"""
Output:

312
312 1
312 1
[0, 1, 0, 0, 0, 0]
327
327 1
327 1
[0, 1, 0, 0, 0, 0]
314
314 1
314 5
[0, 1, 0, 0, 0, 1]
Enter q to Exit or Enter the email: cat
Spam eMail ID!!
Enter q to Exit or Enter the email: hello
Congratulations!!
Enter q to Exit or Enter the email: mushrifah
Congratulations!!
Enter q to Exit or Enter the email: q

"""
