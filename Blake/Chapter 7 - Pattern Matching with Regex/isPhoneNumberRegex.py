#! python3
# isPhoneNumber with Regex from Chapter 7

import re

def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
    matchObject = phoneNumRegex.search(text)
    if matchObject == None:
       return False
    else:
        return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('555-4242 is a phone number:')
print(isPhoneNumber('555-4242'))
print('(415) 555-4242 is a phone number:')
print(isPhoneNumber('(415) 555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))
