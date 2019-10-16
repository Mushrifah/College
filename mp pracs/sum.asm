include macro.asm
data segment
n1 db 05h
n2 db 06h
res db 20 dup(00h)
data ends

code segment
assume cs:code, ds:data
start:
mov ax,data
mov ds,ax

sum n1,n2,res
int 03h

code ends
end start