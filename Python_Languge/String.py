# string is immutable


name = 'Govind'
print(name)

print(len(name))

print(name.endswith('nd'))

print(name.capitalize()) # lower , upper also method's of string

index = name.find("vind")
print(index)

replaced_string = name.replace("d", "d Khedkar")
print(replaced_string)


str = "govind is good \"boy\""
print(str)


letter = '''Dear |<name>|
you are selected!
|<date>|'''

print(letter.replace("|<name>|", "Govind").replace("|<date>|", "13 may 2025"))

name = "Govind is good boy  and"
print(name.replace("  ", " "))
print(name)

