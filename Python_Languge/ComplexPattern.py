'''
Program for printing following pattern

*          **          *
**      **    **      **
***  ***        ***  ***
*******          *******
***  ***        ***  ***
**      **    **      **
*          **          *

''' 

n = int(input("Enter a number of row you want for pattern "))
if(n%2==0):
    n = n-1

half = n//2

for i in range (1,n+1):
    if(i<=half):
        print("*"*i+" "*((n-i*2)*2)+"*"*i+" "*(i*2-2)*2+"*"*i+" "*((n-i*2)*2)+"*"*i)
    elif(i==half+1):
        print("*"*n+" "*(i*2-3)*2+"*"*n)
    else:
        j = n+1-i
        print("*"*j+" "*((n-j*2)*2)+"*"*j+" "*(j*2-2)*2+"*"*j+" "*((n-j*2)*2)+"*"*j)

