;case of string
data segment 
src db 'Hello World$' 
data ends 

extra segment 
dest db 20 dup(0) 
extra ends 

code segment 
assume cs:code,ds:data,es:extra 
start: mov ax,data 
          mov ds,ax 
          mov ax,extra 
         mov es,ax 
          cld 
         lea si,src 
         lea di,dest 
  up: lodsb 
        cmp al,'$' 
        jz exit 
        cmp al,40h 
        jna skip 
        cmp al,59h 
        jbe convert 
        cmp al,60h 
        jna skip 
        cmp al,79h 
        jnbe skip 
        sub al,20h 
        jmp skip 
convert:add al,20h 
 skip:stosb 
         jmp up 
exit:int 03h 
code ends 
end start
