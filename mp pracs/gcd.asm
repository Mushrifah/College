;gcd of number
#include<stdio.h>
#include<conio.h>
void main()
{
int a,b,c;
clrscr();
printf("Enter the two numbers\n");
scanf("%d%d",&a,&b);
asm{
    mov ax,a
    mov bx,b
    }
bck:
asm{
    cmp ax,bx
    jc sec
    }
first:
asm{
    sub ax,bx
    jmp ck
    }
sec:
asm sub bx,ax
ck:
asm{
    cmp ax,bx
    jnz bck
    mov c,ax
    }
printf("The gcd is %d",c);
getch();
}
