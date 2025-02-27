def merge_the_tools(string, k):
    t = [string[i:i+k] for i in range(0, len(string), k)]
    for i in range(0,len(t)):
        seen = set()
        result = ""
        for char in t[i]:
            if char not in seen:
                seen.add(char)
                result += char
        print(result)






        
        

if __name__ == '__main__':
    print("Enter string")
    string = input()
    print("Enter value of k")
    k = int(input())
    merge_the_tools(string, k)