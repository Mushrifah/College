data segment
src db 01h,02h,03h,04h,05h,06h,07h,08h,09h,0ah
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
    jnc down
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
