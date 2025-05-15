'''Keylogger Decoder
Sample Input: 1234
Sample Output:
abcd
awd
lcd
'''

def KeyloggerDecoder(input_digits):
    result = []

    def helper(index, path):
        if index == len(input_digits):
            result.append(path)
            return

        # Take 1 digit
        num1 = input_digits[index]
        if 1 <= num1 <= 9:
            letter = chr(ord('a') + num1 - 1)
            helper(index + 1, path + letter)

        # Take 2 digits
        if index + 1 < len(input_digits):
            num2 = input_digits[index] * 10 + input_digits[index + 1]
            if 10 <= num2 <= 26:
                letter = chr(ord('a') + num2 - 1)
                helper(index + 2, path + letter)

    helper(0, "")
    return sorted(result)


input = [1, 2, 3, 4]
print("Original Numbers:", input)
print("The key loggers of numbers:")
for word in KeyloggerDecoder(input):
    print(word)
