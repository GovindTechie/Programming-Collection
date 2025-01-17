#include <stdio.h>

void main()
{
  
 long long int n=0,i,m=1,j,fib=0 ;  
  printf("enter number");
  scanf("%Ld",&j);
   {
  printf("Fibonacci sequence 1 is: 0 \n");
  printf("Fibonacci sequence 2 is: 1 \n");
  }
  
  for(i=3;i<=j;i++)
  {
    fib=n+m;
    n=m;
    m=fib;
    printf("Fibonacci sequence %Ld is: %Ld \n",i,fib);
    
  }
 }
  
  