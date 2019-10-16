data segment
src db 0ah,09h,08h,07h,06h,05h,04h,03h,02h,01h
count db 0ah
data ends
code segment
assume cs:code,ds:data
start:mov ax,data
      mov ds,ax
      mov cl,count
up1:mov ch,cl
    lea si,src
up: mov al,[si]
    mov ah,[si+1]
    cmp al,ah
    jc down
    xchg al,ah
    mov [si],al
    mov [si+1],ah
down:inc si
     dec ch
     jnz up
     dec cl
     jnz up1
int 03h
code ends
end start
