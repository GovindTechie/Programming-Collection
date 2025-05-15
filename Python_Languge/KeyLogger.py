def keylogger_decoder(s):
    result = []

    def dfs(index, path):
        if index == len(s):
            result.append(path)
            return

        if s[index] == '0':
            return

        num1 = int(s[index])
        if 1 <= num1 <= 9:
            dfs(index + 1, path + chr(ord('A') + num1 - 1))

        if index + 1 < len(s):
            num2 = int(s[index:index + 2])
            if 10 <= num2 <= 26:
                dfs(index + 2, path + chr(ord('A') + num2 - 1))

    dfs(0, "")
    return result

# ---- Function Calling ----
input_str = input("Enter the digit string: ")
outputs = keylogger_decoder(input_str)

print("Possible decodings are:")
for word in outputs:
    print(word)
