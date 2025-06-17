marks = {
    "Govind" : 98,
    "Mukund" : 97,
    "Veer" : 95
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Govind":99})
print(marks)


# print(marks["Govind2"]) # print error
print(marks.get("Govind2")) # prints none

new_dic = marks.copy()
print(f"New Dictonory is : {new_dic} ")