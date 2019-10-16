data segment
hr db 9
mi db 32
se db 45
data ends
code segment
assume cs:code,ds:data
start:mov ax,data
mov ds,ax
mov ch,hr
mov cl,mi
mov dh,se
mov ah,2dh
int 21h
int 03h
code ends
end start
