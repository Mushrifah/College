include <iostream.h>
#include <conio.h>
void main()
{
clrscr();
int a,b,temp;
cout<<"Please enter first number:"<<endl;
cin>>a;
cout<<"Please enter second number:"<<endl;
cin>>b;
cout<<endl;
temp = a;
asm mov ax,a
asm mov bx,b
bck:
asm cmp ax,0000h
asm jz ex
asm cmp bx,0000h
asm jz ex
asm div bl
asm cmp ah,00h
asm jz ex
temp = temp + a;
asm mov ax,temp
asm mov bx,b
asm jmp bck
ex:
cout<<"The LCM is: "<<temp;
getch();
}