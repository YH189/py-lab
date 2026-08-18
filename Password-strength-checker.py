def check_password_strength(password):
    if len(password) < 8:
        return "Weak"

    upper = False
    lower = False
    number = False
    special = False

    for char in password:
        if char.isupper():
            upper = True
        if char.islower():
            lower = True
        if char.isdigit():
            number = True
        if not char.isalnum():
            special = True

    if upper and lower and number and special:
        return "Strong"
    elif upper and lower and number:
        return "Medium"
    else:
        return "Weak"


print(check_password_strength("user7890"))
print(check_password_strength("Password@1090"))
print(check_password_strength("00000000"))
