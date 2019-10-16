data segment
msg1 db 10,13,'Enter first number',10,13,'$'
msg2 db 10,13,'Enter second number',10,13,'$'
msg3 db 10,13,'Screen is successfully cleared$'
data ends

code segment
assume cs:code,ds:data
start:mov ax,data
      mov ds,ax
      lea dx,msg1
      mov ah,09h
      int 21h
     mov ah,01h
      int 21h
     mov ah,01h
      int 21h
     mov ax,0600h
      mov bh,71h
      mov cx,0000h
      mov dx,184Fh
      int 10h

      lea dx,msg2
      mov ah,09h
      int 21h
     mov ah,01h
      int 21h
     mov ah,01h
      int 21h
     mov ax,0600h
      mov bh,71h
      mov cx,0000h
      mov dx,184Fh
      int 10h

      lea dx,msg3
      mov ah,09h
      int 21h
      mov ah,01h
      int 21h
     mov ah,01h
      int 21h
    mov ax,0600h
      mov bh,71h
      mov cx,0000h
      mov dx,184Fh
      int 10h
int 03h
code ends
end start
