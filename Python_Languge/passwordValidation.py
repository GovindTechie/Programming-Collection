'''
Password Validaon
• At least 4 characters long.
• Contains at least one numeric digit.
• Contains at least one uppercase leer.
• Does not contain spaces or slashes ('/').
• Does not start with a digit.

Sample Input:
aA1_67
Sample Output:
password valid
'''

def passwordValid(str):
    if len(str) < 4:
        return "Invalid password, try again"
    if " " in str or '/' in str:
        return "Invalid password, try again"
    if str[0].isdigit():
        return "Invalid password, try again"
    if not any(char.isdigit() for char in password):  
        return "Invalid password, try again"
    if not any(char.isupper() for char in password):
        return "Invalid password, try again"
    
    return "Password Valid"



password = "1aA1_67"
print(f"Original password : {password}")
print(f"is valid : {passwordValid(password)}")