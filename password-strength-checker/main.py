import string

print('------------------ Password Strength Checker ------------------')
password = input("Enter a password to check: ")
score = 0

# Check length criteria
if len(password) >= 8:
    print('You have passed the minimum length criteria.')
    score += 1
else:
    print('You should have at least 8 characters.')
    score -= 1

# Check for numbers
if any(char.isdigit() for char in password):
    score += 1
else:
    print('Your password should have an integer.')
    score -= 1

# Check for uppercase letters
if any(char.isupper() for char in password):
    score += 1
else:
    print('Password should contain at least 1 capital letter.')

# Check for lowercase letters
if any(char.islower() for char in password):
    score += 1
else:
    print('Password should contain at least 1 small letter.')

# Check for special characters
if any(char in string.punctuation for char in password):
    print('Special character check passed.')
    score += 1
else:
    print('Password should contain at least 1 special character (e.g., @, #, $).')

print(f'Final Score: {score}')
