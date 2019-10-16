data segment
dname db "E:\MPE",0
data ends
code segment
assume cs:code,ds:data
start: mov dx,seg dname
mov ds,dx
mov dx,offset dname
mov ah,3ah
int 21h
int 03h
code ends
end start
