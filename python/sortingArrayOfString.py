'''
Sorng an Array of Strings by Length
'''

# # simple approach
# def sortingArrayOfStringByLength(arr):
#     return sorted(arr, key=len)


def sortingArrayOfStringByLength(arr):
    sorted_arr = []
    while arr:
        smallest = arr[0]
        for word in arr:
            if len(word) < len(smallest) or (len(word) == len(smallest) and word < smallest):
                smallest = word
        sorted_arr.append(smallest)
        arr.remove(smallest)
    return sorted_arr


n = 4
arr = ["apple", "bat", "car", "elephant"]
print(f'Original array of strings : {arr}')
print(f"After soting arr according to string length : {sortingArrayOfStringByLength(arr)}")


