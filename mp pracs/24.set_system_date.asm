data segment
yr dw 2015
mo db 07
dy db 04
data ends
code segment
assume cs:code,ds:data
start:mov ax,data
mov ds,ax
mov cx,yr
mov dh,mo
mov dl,dy
mov ah,2bh
int 21h
int 03h
code ends
end start
