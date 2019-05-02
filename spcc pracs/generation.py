#infixexp = "a*b*c/d-e/f"
infixexp = "a*b*c/d-e/f*g+h"
pointer = 0
replace = ["Z","Y","X","W","V","U","T","S","R","Q","P"]
l2=len(infixexp)
l=infixexp.count("/")
for  i in range(0,l) :
    position = infixexp.index("/")
    print(replace[pointer] + ":=" + infixexp[position - 1:position + 2])
    infixexp = infixexp[0:position-1] + replace[pointer] + infixexp[position+2:l2]
    pointer = pointer + 1

l=infixexp.count("*")
for  i in range(0,l) :
    position = infixexp.index("*")
    print(replace[pointer] + ":=" + infixexp[position - 1:position + 2])
    infixexp = infixexp[0:position-1] + replace[pointer] + infixexp[position+2:l2]
    pointer = pointer + 1


l=infixexp.count("-")
for  i in range(0,l) :
    position = infixexp.index("-")
    print(replace[pointer] + ":=" + infixexp[position - 1:position + 2])
    infixexp = infixexp[0:position-1] + replace[pointer] + infixexp[position+2:l2]
    pointer = pointer + 1


l=infixexp.count("+")
for  i in range(0,l) :
    position = infixexp.index("+")
    print(replace[pointer] + ":=" + infixexp[position - 1:position + 2])
    infixexp = infixexp[0:position-1] + replace[pointer] + infixexp[position+2:l2]
    pointer = pointer + 1
print(infixexp + ":=" + replace[pointer])
