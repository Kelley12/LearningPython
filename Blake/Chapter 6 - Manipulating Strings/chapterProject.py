#! python3
# Chapter Project from Chapter 6: Password Locker
# An insecure password locker

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys,pyperclip
if len(sys.argv) < 2:
    print('Usage: python chapterProject.py [account] - copy acccount password')
    sys.exit()

account = sys.argv[1] # first command line argument should be the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
