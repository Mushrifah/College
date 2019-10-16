;convert into uppercase 
data segment
src db 'Hello World$'
data ends
extra segment
dest db 20 dup(0)
extra ends
code segment
assume cs:code,ds:data,es:extra
start:mov ax,data
    mov ds,ax
    mov ax,extra
    mov es,ax
    cld
    lea si,src
    lea di,dest
up:lodsb
   cmp al,'$'
   jz exit
   cmp al,20h
   je skip
   cmp al,41h
   jbe skip
   cmp al,5ah
   jbe skip
   sub al,20h
skip:stosb
jmp up
exit:int 03h
code ends
end start
