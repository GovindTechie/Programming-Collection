# Remove all Special Characters “"Artificial %#$@ Intelligence $123"

def RemoveSpecialChar(string):
    return ''.join (char for char in string if char.isalnum() or char.isspace())

string = "Artificial %#$@ Intelligence $123"
print(f"Original String : {string}")
print(f"After remove Special Character : {RemoveSpecialChar(string)}")
