data segment
yr dw ?
mo db ?
dy db ?
data ends
code segment
assume cs:code,ds:data
start:mov ax,data
mov ds,ax
mov ah,2ah
int 21h
mov yr,cx
mov mo,dh
mov dy,dl
int 03h
code ends
end start
