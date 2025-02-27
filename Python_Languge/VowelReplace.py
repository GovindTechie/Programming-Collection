# Replace all Vowels by ‘#’ input String : "hello world"

string = "hello world"
list = list(string)

for i in range(0, len(list)):
    if list[i].lower() in ('a', 'e', 'i', 'o', 'u'):
        list[i] = '#'

replacedString = "".join(list)
print(f"Replaced String: {replacedString}")