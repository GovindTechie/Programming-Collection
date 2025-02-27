'''Sum of Digits in a String:
Problem: Write a program that reads a string containing both letters and
digits, and calculates the sum of all the digits present in the string.
Example:
▪ Input: "abc123xyz"
▪ Output: 6
'''

string = input("Enter a string ")
sum = 0
for char in string:
    if char.isnumeric():
        sum += int(char)
print(f"String is : {string}")
print(f"Sum of digits in string : {sum}")