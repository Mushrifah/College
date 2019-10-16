data segment
msg1 db 10,13,'Even Number$'
msg2 db 10,13,'Odd Number$'
msg3 db 10,13,'Enter the number 0-9 or q for quit $'
data ends
code segment
assume cs:code,ds:data
start:mov ax,data
mov ds,ax
up:lea dx,msg3
mov ah,09h
int 21h
mov ah,01h
int 21h
cmp al,'q'
je exit
cmp al,30h
jl up
cmp al,39h
jg up
sub al,30h
shr al,01h
jc odd
lea dx,msg1
jmp skip
odd:lea dx,msg2
skip:mov ah,09h
int 21h
jmp up
exit:mov ah,4ch
int 21h
code ends
end start
