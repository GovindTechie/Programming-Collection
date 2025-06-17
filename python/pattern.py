n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i == 1 or i == n:  # Print full row of stars for first & last row
        print("* " * n)
    else:  # Print first & last star, with spaces in between
        print("* " + "  " * (n - 2) + "*")
