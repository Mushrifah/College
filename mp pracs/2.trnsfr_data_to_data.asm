data segment
src db 01h,02h,03h,04h,05h,06h,07h,08h,09h,0ah,10h,11h,12h,13h,14h,15h,16h,17h,18h,19h
data ends
code segment
assume cs:code,ds:data
start:
mov ax,data
mov ds,ax
lea si,src
mov di,5000h
mov cl,14h
up:mov al,[si]
mov [di],al
inc si
inc di
dec cl
jnz up
int 03h
code ends
end start
