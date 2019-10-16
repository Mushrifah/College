include sum.asm
data segment
n1 db 01h,02h,03h,04h,05h
sum db 00h
data ends
code segment
assume cs:code,ds:data
START:	mov ax, data
		mov ds,ax
		sum n1,sum
		int 03h
	code ends
end START
