%{
	#include<stdio.h>
%}
%token LETTER DIGIT

%%
s:LETTER e
e:LETTER e
|DIGIT e
|
%%
int main()
{
	printf("program to recognize valid\n");
  	if(!yyparse())
  	{
		printf("Valid\n"); 
       	}
}
int yyerror()
{
 	printf("Invalid\n");
}
/*

yaac -d b.y
gcc lex.yy.c y.tab.c -ll 
./a.out 

ryms@ryms-ThinkCentre-M72e:~/Desktop$ ./a.out
program to recognize valid
husain123
Valid
ryms@ryms-ThinkCentre-M72e:~/Desktop$ ./a.out
program to recognize valid
123husain
Invalid
*/

