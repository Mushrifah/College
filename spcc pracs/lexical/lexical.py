from typing import List

keyword = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern",
           "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static",
           "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "printf"]
operator = ["+", "-", "*", "/", "%", "++", "--", "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "&", "|", "^", "~",
            ">>", "<<", "=", "+=", "-=", "*="]
bracket = ["{", "}", "[", "]", "(", ")"]
digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
ide=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

kf = []
opf = []
bkf = []
impf = []
idf = []
conf = []
fn = "myprog.c"
f = open(fn, "r+")
for l in f:
    ls = list(l.split(" "))
    for i in range(0, len(ls)):
        d = ls[i]
        if ls[i] in keyword:
            if ls[i] not in kf:
                kf.append(ls[i])

        elif ls[i] in operator:
            if ls[i] not in opf:
                opf.append(ls[i])

        elif ls[i] in bracket:
            if ls[i] not in bkf:
                bkf.append(ls[i])

        elif ls[i] in ide:
            if ls[i] not in idf:
                idf.append(ls[i])

        elif ls[i] != ";" and ls[i] != "\n" and ls[i] != "," and ls[i] != "":
            v = ls[i]
            if v[0] != "\"":
                v = list(ls[i].split("."))
                if len(v) is 2:
                    if ls[i] not in impf:
                        impf.append(ls[i])
                elif len(d) != 0:
                    if d[0] in digit:
                        if ls[i] not in conf:
                            conf.append(ls[i])
                else:
                    if ls[i] not in idf:
                        idf.append(ls[i])

f.close()
print("Keywords: " + str(kf))
print("Identifier: " + str(idf))
print("Import Statements: " + str(impf))
print("Operators: " + str(opf))
print("Number: " + str(conf))
print("Brackets: " + str(bkf))



'''
OUTPUT
Keywords: ['void', 'int', 'printf']
Identifier: ['a']
Import Statements: ['#include<stdio.h>']
Operators: ['=', '*']
Number: ['1', '25']
Brackets: ['(', ')', '{', '}']

'''

