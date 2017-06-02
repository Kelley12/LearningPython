while True:
    print('You are...?')
    name = input()
    if name != 'Jess':
        continue
    print('Hi Jess. What\'s the secret code? (It\'s smelly.)')
    password = input()
    if password == 'swordfish':
        break
    print('Welcome back.')
