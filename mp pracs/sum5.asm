sum macro arg1,arg2
	mov al,arg2
	lea si,arg1
	mov cl,05h
up:	add al,[si]
	inc si
	dec cl
	jnz up
endm
