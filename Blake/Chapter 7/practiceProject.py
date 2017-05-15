#! python3
# Practice Project from Chapter 7: Strong Password Checker
# Checks a password for password requirements

import re

# Create Strong Password regex
lowerCaseRegex = re.compile(r'[a-z]+')  # At least 1 lower case letter
upperCaseRegex = re.compile(r'[A-Z]+')  # At least 1 upper case letter
numericRegex = re.compile(r'[0-9]+')    # At least 1 number

# Strong Password Detection
def strongPassword(password):
    if len(password) < 8:
        print('Password length too short. Must be at least 8 characters.')
        return False
    elif lowerCaseRegex.search(password) == None:
        print('No lower case characters.')
        return False
    elif upperCaseRegex.search(password) == None:
        print('No upper case characters.')
        return False
    elif numericRegex.search(password) == None:
        print('No numeric characters.')
        return False
    else:
        print("Password Meets minimum requirements")
        return True


password = '123XYZ789'
print('Checking password strength: ' + password)
strongPassword(password)

password = '123abc789'
print('Checking password strength: ' + password)
strongPassword(password)

password = 'abcdEfGXYZ'
print('Checking password strength: ' + password)
strongPassword(password)

password = '123abcX'
print('Checking password strength: ' + password)
strongPassword(password)

password = '123abcXYZ789'
print('Checking password strength: ' + password)
strongPassword(password)
