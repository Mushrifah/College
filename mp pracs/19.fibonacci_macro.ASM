fibo macro n1,res
mov al,n1
lea si,res
mov [si],al
inc si
dec n1
jz exit
mov al,01h
mov ah,0h
up:
add al,ah
mov [si],al
inc si
xchg al,ah
dec n1
jnz up
exit:int 03h
 endm