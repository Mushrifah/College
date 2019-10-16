data segment
no db 05h
fact dw ?
data ends

code segment
assume cs:code, ds:data
start:
mov ax,data
mov ds,ax
mov bl,no
call factorial
mov fact,ax
int 03h

factorial proc near
mov ax,01h
up:
mul bx
dec bx
jnz up
ret
factorial endp

code ends
end start

