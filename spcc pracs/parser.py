n=int(input("Enter number of productions: "))
production_lhs=[""*i for i in range (n)]
production_rhs=[""*i for i in range (n)]
stack=""
for i in range (n):
    production_lhs[i]=input("Enter lhs of production ")
    production_rhs[i] = input("Enter rhs of production ")
print("Productions are: ")
for i in range(n):
    print(production_lhs[i],"->",production_rhs[i])
expression=input("Enter expression: ")
exp_list=expression.split(" ") #expression has whitespace
for i in range(len(exp_list)):
    temp=exp_list[i] #scan every individual element in expr
    for j in range(n):
        if(temp==production_rhs[j]):
            temp=production_lhs[j] #find corresponding production rule for scanned item
            break
    stack = stack + temp #update stack
    print("Content of stack is: ",stack)
    for j in range(n):
        if(stack==production_rhs[j]):
            stack=production_lhs[j] #reduce stack
            break
print("Content of stack is: ",stack)
if(stack==production_lhs[0]):
    print("Accepted")
else:
    print("Rejected")
