;search a number
data segment 
src db 01h,02h,03h,04h,05h,06h,07h,08h,09h,0Ah 
count db 0Ah 
search db 05h
found db 01h 
data ends 
code segment 
assume cs:code,ds:data 
start:mov ax,data 
         mov ds,ax 
         lea si,src 
up:   mov al,[si]  
        cmp search,al 
        jz exit 
        inc si 
        dec count 
        jnz up 
        mov found,00h  
exit:int 03h 
code ends 
end start