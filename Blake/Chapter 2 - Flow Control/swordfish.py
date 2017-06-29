# swordfish from Chapter 2

while True:
    print('Please type your name:')
    name = input()
    if name != 'Blake':
        continue
    print('Hello Blake. What is the password? (Type of fish)')
    if password == 'swordfish':
        break
print('Access granted.')
