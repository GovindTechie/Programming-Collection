from itertools import product


def letterCombinations(digits):
    if not digits:
        return []

    digit_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    letterList = [digit_to_letters[d] for d in digits]
    combinations = [''.join(p) for p in product(*letterList)]
    return combinations

digits = "23"
print(f"Original digit : {digits}")
print(f"Letter combination : {letterCombinations(digits)}")
