def print_rangoli(size):
    alph = [chr(97 + i) for i in range(size)]  # List of alphabets ['a', 'b', 'c', ...]
    width = (size * 4) - 3  # Width of the rangoli
    
    # Generate the rows
    for i in range(size - 1, -1, -1):  # From size-1 to 0
        row = '-'.join(alph[i:size])  # Characters in the row
        print((row[::-1] + row[1:]).center(width, '-'))  # Reflect and center

    # Mirror the rows
    for i in range(1, size):  # Rows from 1 to size-1
        row = '-'.join(alph[i:size])
        print((row[::-1] + row[1:]).center(width, '-'))

if __name__ == '__main__':
    n = int(input("Enter size: "))
    print_rangoli(n)



























# def print_rangoli(size):
#     alph = 97+size
#     for i in range(0,size//2):
#         print("e".center())
        

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)