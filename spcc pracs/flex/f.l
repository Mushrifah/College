%{
int count=0;
%}
op [+-*/]
letter [a-zA-Z]
number [0-9]
id ({letter}*|"_")*|({letter}{number})*
notid({number}{letter})*
%%
[\t\n]*
("int")|("char")|("float")|("if") {printf("%s is a keyword\n",yytext);}
{id} {printf("%s is an identifier\n",yytext);count++;}
{notid} {printf("%s is not an identifier\n",yytext);}

%%
int main()
{
FILE *fp;
char file[10];
printf("\nEnter the file name : ");
scanf("%s", file);
fp=fopen(file,"r");
yyin=fp;
yylex();
printf("Total no of identifiers are : %d\n",count);
return 0;
}
/*Outputryms@ryms-ThinkCentre-M72e:~$ flex f.l
ryms@ryms-ThinkCentre-M72e:~$ cc lex.yy.c -ll -o first
ryms@ryms-ThinkCentre-M72e:~$ cat >flex
int 
husain
_hsp
786h
if
char

ryms@ryms-ThinkCentre-M72e:~$ ./first

Enter the file name : flex
int is a keyword
husain is an identifier
_hsp is an identifier
786h is not an identifier
if is a keyword
char is a keyword
Total no of identifiers are : 2

*/

