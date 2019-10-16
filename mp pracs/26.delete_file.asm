data segment
dname db 'D:\doc\ABC',0
data ends
code segment
assume cs:code,ds:data
start:mov ax,data
mov ds,ax
mov dx,seg dname
mov ds,dx
mov dx,offset dname
mov ah,41h
int 21h
code ends
end start
