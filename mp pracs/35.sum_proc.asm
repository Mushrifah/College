data segment
n1 db 05h
n2 db 06h
res dw ?
data ends

code segment
assume cs:code, ds:data
start:
mov ax,data
mov ds,ax
call sum
mov res,ax
int 03h

sum proc near
add ax,bx
ret
sum endp

code ends
end start