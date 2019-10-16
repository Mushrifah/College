data segment
hours db ?
mins db ?
sec db  ?
msec db  ?
data ends
code segment
assume cs:code,ds:data
start:mov ax,data
mov ds,ax
mov ah,2ch
int 21h
mov hours,ch
mov mins,cl
mov sec,dh
mov msec,dl
int 03h
code ends
end start
