data segment
src db 'husain$'
palin db 01h
data ends

extra segment
rev db 8 dup (00h)
extra ends

code segment
assume cs:code,ds:data,es:extra
start:mov ax,data
         mov ds,ax
         mov ax,extra
         mov es,ax
         mov cl,00h
         lea si,src
         lea di,rev
        cld
  up:lodsb
        cmp al,'$'
        je revrs
        inc cl
        jmp up
        mov ch,cl
revrs:sub si,0002h
cont:std
          lodsb
          cld
          stosb
          dec ch
          jnz cont
          lea di,rev
          lea si,src
          cld
          repe cmpsb
cmp cx,0000h
je exit
mov palin,00h
exit:int 03h
code ends
end start
