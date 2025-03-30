'''
Lexicographically Smallest and Largest Substring
Problem Statement:
Given a string S and an integer K, find the lexicographically smallest and
largest
substrings of length K.
Input:
S = "welcometojava"
K = 3
Output:
Smallest: "ava"
Largest: "wel"
'''


def lexicographicallySmallestLargest(S, K):
    substrings = [S[i:i+K] for i in range(len(S) - K + 1)]
    substrings.sort()
    return substrings[0], substrings[-1]

S = "welcometojava"
K = 3
smallest, largest = lexicographicallySmallestLargest(S, K)
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
