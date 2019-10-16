data segment
no1 db 08h,14h,05h,0Fh,09h,01h,20h,05h,03h,07h
count db 0Ah
large db ?
data ends
code segment
assume cs:code, ds:data
start: mov ax, data
mov ds, ax
mov al, 00h
LEA si, no1
up:
mov ah, [SI]
cmp al, ah
jnc continue
mov al, ah
continue:
inc si
dec count
jnz up
 
mov large,al
int 03h
code ends
end start