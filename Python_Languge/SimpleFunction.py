def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))

    return n

l = ["Govind", "Mukund", "Veer", "Atharv"]
print(rem(l, "Atharv"))