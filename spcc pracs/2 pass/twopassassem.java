import java.io.*;
import java.lang.*;
class twopassassem
{
    public static void main(String args[])throws IOException
    {
	DataInputStream in=new DataInputStream(System.in);
		
	String inp[]=new String[50];
	String str[]=new String[30];
	String bt[][]=new String[16][16];
	String st[][]=new String[15][4];
	String lt[][]=new String[15][4];
	String pass1[][]=new String[30][2];
	String pass2[][]=new String[30][2];
	String str1="",str2="using",dc="DC",a="",apos="'",str3="",ds="DS";
	String f="F",equ="EQU",end="END",sr="SR",equal="=";
	String bin="",r1="";
	int count=0,chk8,chk6,chk5,chk4,chk9;
	int lc=0,chk,chk1,n=0,o=0;
	int add1[]=new int[50];
			
	for(int i=0;i<30;i++)
		str[i]="";
		
	int k=0,l=0,x=0,o1=0,reg=0,c1=0,z=0,oi=0;
	System.out.println("\n<<<ENTER PROGRAM>>>");
	for(int i=0;i<50;i++)
	{
		inp[i]=in.readLine();
	
		if(inp[i].length()==1)
		{
			k=i;
			break;
		}
	}
	while(l<k)
	{
		String symb="";
		for(int i=0;i<inp[l].length();i++)
		{
			if(inp[l].charAt(i)!=' ')
			symb=symb+inp[l].charAt(i);
		else
		{
	        	if(symb.charAt(0)!='#')
		{
			st[z][0]=symb;
		}
			break;
		}
		}
		if(l>0)
		{
			for(int i=0;i<inp[l].length();i++)
		{
			if(inp[l].charAt(i)==',')
			{
			   o=i;
			   oi=i-1;
			   o1=i+1;
			   break;	
			}
		}						
		chk=inp[l].indexOf(str2);
		chk6=inp[l].indexOf(equ);
		chk8=inp[l].indexOf(ds);
		chk5=inp[l].indexOf(end);
		chk4=inp[l].indexOf(sr);
		chk9=inp[l].indexOf(equal);
		
		if(chk9!=-1)
		{
			String lit="";
			for(int m=chk9+1;m<inp[l].length();m++)
			lit=lit+inp[l].charAt(m);
			lt[n][0]=lit;
			int chk11=lit.indexOf(apos);
			chk11=chk11+1;
			String strng="";
			while(lit.charAt(chk11)>='0'&&lit.charAt(chk11)<='9')
			{
				strng=strng+lit.charAt(chk11);
				chk11++;
			}
			String a1;
      for (int h = 0;h<strng.length();h++)
      {
	a1=Integer.toBinaryString(Character.digit(strng.charAt(h),16));
			
		if(a1.length()<4)
		{
			int b=(4-a1.length());
			for(int j=0;j<b;j++)
			a1="0"+a1;
		}
			bin=bin+a1;
   	 }	
      }
	if(chk6!=-1||chk5!=-1)
	{
		lc=lc+add1[l-1];
		String lc1 = new Integer(lc).toString();
		pass1[l][0]=lc1;
		pass2[l][0]=lc1;
		add1[l]=0;
		pass1[l][1]="";
		if(chk5!=-1)
	  		pass2[l][1]=bin;
		else
			pass2[l][1]="";
		if(chk5!=-1)
		{
			lt[n][1]=lc1;
			lt[n][2]="4";
			lt[n][3]="R";
			n++;
		}
		
		if(chk6!=-1)
		{
			st[z][1]=lc1;
			st[z][2]="1";
			st[z][3]="A";
			z++;
		}
		}
		int c2=0;
		String p1="";
		while(c2<=2&&o!=0&&chk==-1&&chk8==-1)
		{
			p1=inp[l].charAt(o)+p1;
			o--;
			if(inp[l].charAt(o)==' ')
			c2++;
		}
		if(c2==2)
		{
			if(chk4==-1)
			{
				pass2[l][1]=p1;
				p1=p1+"___";
				pass1[l][1]=p1+"___";
			}
			else
			{
				chk4=chk4;
				String sr1="";
				int f1=inp[l].length()-1;
			while(f1!=chk4-1)
			{
				sr1=inp[l].charAt(f1)+sr1;
				f1--;
			}
				pass1[l][1]=sr1;
				pass2[l][1]=sr1;
			}
			
		String s1="";
		if(chk!=-1&&chk8==-1)
		{
			lc=lc;
			add1[l]=0;			
		}
		else
		{
		  for(int i=o1;i<inp[l].length();i++)
		  s1=s1+inp[l].charAt(i);
						
		if(s1.charAt(0)>='0'&&s1.charAt(0)<='9')
			add1[l]=2;
		else
			add1[l]=4;
		}
		lc=lc+add1[l-1];
		String lc1 = new Integer(lc).toString();
			pass1[l][0]=lc1;
			pass2[l][0]=lc1;
		}
		else if(chk!=-1)
		{
		   for(int i=o1;i<inp[l].length();i++)
		   str3=str3+inp[l].charAt(i);
					
		   String str22="";
		while(inp[l].charAt(oi)!=' ')
		{
			str22=inp[l].charAt(oi)+str22;
			oi--;
			if(oi<=-1)
			break;
		}
		if(str3.charAt(0)>='0'&&str3.charAt(0)<='9')
			reg = Integer.parseInt(str3);
		else
		{
			String str9="";
			for(int q=l+1;q<k;q++)
			{
		  	  int use=inp[q].indexOf(str3);
			  if(use!=-1)
			  {
			    int w=inp[q].length()-1;
			while(inp[q].charAt(w)!=' ')
			{
			str9=inp[q].charAt(w)+str9;
			w--;
			}
		}
		}
		reg=Integer.parseInt(str9);	
		r1=str9;					    
		}
		if(str22.charAt(0)=='*')
			bt[reg][1]="";
		else
		        bt[reg][1]=str22;
					    
			bt[reg][0]="Y";		
					     					    
			str3="";
				    
			add1[l]=0;
			pass1[l][0]="0";
			pass2[l][0]="0";
			pass1[l][1]="";
			pass2[l][1]="";
		}
		else
		{
		  int com=0,chk2=inp[l].indexOf(dc),chk3=inp[l].indexOf(f);
		   if(chk2!=-1)
		   {
			com=inp[l].indexOf(apos);
			com++;
			if(com!=-1)
			{
		  	  String dc1="";
			 while(inp[l].charAt(com)>='0'&&inp[l].charAt(com)<='9')
			{
				dc1=dc1+inp[l].charAt(com);
				com++;
			}
			String bin_a="";
	for (int i = 0;i<dc1.length();i++)
 	{
	
	a=Integer.toBinaryString(Character.digit(dc1.charAt(i),16));
	if(a.length()<4)
	{
  	  int b=(4-a.length());
	  for(int j=0;j<b;j++)
	  a="0"+a;
	}
	bin_a=bin_a+a;
        }

	pass1[l][1]=dc1;
	pass2[l][1]=bin_a;

	lc=add1[l-1]+lc;
	if(chk3!=-1)
		add1[l]=4;
	else
		add1[l]=2;
	String lc1 = new Integer(lc).toString();
	pass1[l][0]=lc1;
	pass2[l][0]=lc1;
				
	st[z][1]=lc1;
	if(add1[l]==4)
		st[z][2]="4";
	else
		st[z][2]="2";
	st[z][3]="R";
	z++;
	}
       }
      }
	if(chk8!=-1&&l!=0)
	{
	  lc=Integer.parseInt(pass1[l-1][0]);
	  lc=lc+add1[l-1];
	   String lc1 = new Integer(lc).toString();
	   pass1[l][0]=lc1;
	   pass2[l][0]=lc1;
	   st[z][1]=lc1;
	   int chk7=inp[l].indexOf(f);
	if(chk7!=-1)
	{
	   add1[l]=4;
	   st[z][2]="4";
	}
	else 
	{
	  add1[l]=2;
	  st[z][2]="2";
	}
	  st[z][3]="R";
	  pass1[l][1]="";
	  pass2[l][1]="";
	  z++;
	}
	  }
	  else
	 {
	    add1[l]=0;
	    pass1[l][0]="0";
	    pass2[l][0]="0";
	    pass1[l][1]="";
	    pass2[l][1]="";
	    st[z][1]="0";
	    st[z][2]="1";
	    st[z][3]="R";
	    z++;
	}
	  l++;
	}
	int l2=0;
	while(l2<k)
	{
	   String under="___",coma=",",txt="";
		
	 int l3=0,chk10=pass1[l2][1].indexOf(under),chk13,l1=0;
	if(chk10!=-1)
	{
	 	String p2=pass2[l2][1];
		int chk12=inp[l2].indexOf(coma);
		chk12++;
		while(chk12<inp[l2].length())
		{
			txt=txt+inp[l2].charAt(chk12);
			chk12++;
			l3=l2+1;
		}
			chk1=inp[l2].indexOf(equal);
	
		if(chk1==-1)
		{
	   	  for(int i=l3;i<k;i++)	
		  {
			chk13=inp[i].indexOf(txt);
			if(chk13!=-1)
			{
				l1=i;
				break;
			}
		}
			p2=p2+pass1[l1][0]+"(0,"+r1+")";
		}
		else
			p2=p2+pass1[k-1][0]+"(0,"+r1+")";
				
		 pass2[l2][1]=p2;
		}
		l2++;
	}
System.out.println("\t\t***** BASE TABLE*****\n");
System.out.println("SR_NO.\t    AVAILIBILITY INDICATOR\t    CONTENT");
for(int i=0;i<15;i++)
	System.out.println(i+"\t\t   NO\t\t\t\t -");
int ztt=15;
System.out.println(ztt+"\t\t   YES\t\t\t\t 00");
System.out.println("\n\t\t***** MOT TABLE*****\n");
System.out.println("\n\tMNEMONIC_OPCODE\t  BINARY_OPCODE\t  INSTRUCTION_VALUE\t INSTRUCTION_LENGTH\t INSTRUCTION_FORMAT\n\n");
System.out.println("\n\t\t***** POT TABLE*****\n");
System.out.println("\n\tPSEUDO_OPCODE\t  ADDRESS_OF_ROUTINE_TO_PROCESS_PSEUDO_OPCODE\n\n");
System.out.println("\n\t\t***** LITERAL TABLE*****\n");
System.out.println("\n\tLITERAL\t  VALUE\t LENGTH\tRELOCATION");
for(int i=0;i<n;i++)
System.out.println("\n\t"+lt[i][0]+"\t "+lt[i][1]+"\t "+lt[i][2]+"\t "+lt[i][3]);

System.out.println("\n\n\t\t***** SYMBOL TABLE*****\n");
System.out.println("\n\tSYMBOL\tVALUE\tLENGTH\tRELOCATION");
for(int i=0;i<z;i++)
	System.out.println("\n\t"+st[i][0]+"\t "+st[i][1]+"\t   "+st[i][2]+"\t   "+st[i][3]);
		
	System.out.println("\n\n\t\t***** P A S S 1 *****\n");	
for(int i=0;i<l;i++)
	System.out.println("\n\t"+inp[i]+"\t\t"+pass1[i][0]+"       "+pass1[i][1]);

System.out.println("\n\n\t\t***** P A S S 2 *****");	
	for(int i=0;i<l;i++)
	System.out.println("\n\t"+inp[i]+"\t\t"+pass2[i][0]+"      "+pass2[i][1]);
   } 
}



