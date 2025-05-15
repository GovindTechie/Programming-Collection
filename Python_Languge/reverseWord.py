def reverseWords(s):
    words = s.strip().split()
    return ' '.join(reversed(words))


input_str = "the sky is blue"
output = reverseWords(input_str)
print("Reversed string:", output)
