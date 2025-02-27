#  i want to print butterfly pattern using python by using single loop , this is challenging but i decide to do it , now see what happen
'''
pattern is following

if n=3
*    *
 *  *
  **
  **
 *  *
*    *

'''

n = int(input("Enter a number for butterfly pattern"))

for i in range (1,(n*2)+1):
    if(i<=n):
        print(" "*(i-1)+"*"+" "*((n-i)*2)+"*")

    else:
        j = (n*2)-i+1
        print(" "*(j-1)+"*"+" "*((n-j)*2)+"*")
