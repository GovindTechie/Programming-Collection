'''Round Table Seating Arrangement:
Problem: Given N members at a round table, where two specific
members must sit next to each other, determine the number of possible
seating arrangements.
Example:
▪ Input: N = 4
▪ Output: 12 
'''

def SeatingPossibility(n):
    def Factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num*Factorial(num-1)
    
    if n < 2:
        return 0
    
    return Factorial(n-1)*2
    


n = int(input("Enter the number of members "))
print(f"Total members : {n}")
print(f"Two seat seating possibility : {SeatingPossibility(n)}")


