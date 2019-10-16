data segment
no1 db 01h,02h,10h,04h,05h,06h,07h,08h,09h,0ah
o1 db ?
e1 db ?
data ends
code segment
assume cs:code,ds:data
start:
mov ax,data
mov ds,ax
mov cl,0ah
lea si,no1
mov ah,00h
up:mov al,[si]
mov bl,02h
div bl
shr ah,1
jc odd1
inc e1
mov bh,e1
jmp cont
odd1:inc o1
mov dh,o1
cont:inc si
dec cl 
jnz up
int 03h
code ends
end start
