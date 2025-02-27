s = {} # empty dictionary
e = set() # empty set

e.add(5)
e.update([5, 6, 3, 6, 1 ,9, 55, 44])
print(e)

e2 = {5, 6, 2, 6, 9, 44}
print(e-e2)