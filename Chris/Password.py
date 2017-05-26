
#Testing password
print ('What is your name?')
Name = input()
print ('What is your password?')
Password = input()

if Name == 'Chris':
    print ('I know you, you are the Magnificent')
    if Password == 'Tadow':
        print ('Access Granted!!')
    else:
        print ('You Suck! Access Denied')
else:
    print ('I do not know you')
