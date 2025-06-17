def sum(n):  # n = 10
    if n == 0:
        return 0
    return n + sum(n-1)



n = int(input("Enter a number for natural number sum : "))
print(f"natural number sum is {sum(n)}" )
    