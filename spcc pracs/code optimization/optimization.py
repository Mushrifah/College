f = open("text.txt","r+")
rhs=[]
lhs=[]
for l in f:
    ls = l.split("=") # temp1=a-b\n, ls[0]=temp1 and ls[1]=a-b/n
    expr2 = ls[1].split("\n") # expr2[0] = a-b, expr2[1]= " "
    ls[1]=expr2[0]
    if(len(lhs)==0): #first line
        lhs.append(ls[0]) #lhs = temp1
        rhs.append(ls[1]) #rhs = a-b

    else:
        checker = 0 # to check if rhs is substitutable
        for i in range (len(lhs)):
            if (rhs.count(ls[1])): #check if current rhs is directly substitutable, if so then leave it
                checker = 1
                break
            elif (ls[1].find(rhs[i])!= -1): #check if current rhs has substitutable part in equation
                lhs.append(ls[0])
                expr = ls[1]
                expr = expr.replace(rhs[i],lhs[i]) #replace rhs part with previous lhs
                rhs.append(expr)
                checker = 1
                break
        if(checker == 0): #if equation is completely new then leave
            lhs.append(ls[0])
            rhs.append(ls[1])
for i in range (len(lhs)):
    print(lhs[i],"=",rhs[i])

