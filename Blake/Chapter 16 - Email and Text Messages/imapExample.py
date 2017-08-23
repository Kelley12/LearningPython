#! python3
# imapExample.py - Internet Message Access Protocol (IMAP) specifies how to communicate with an email provider’s
# server to retrieve emails sent to your email address

# requires the installation of imapclient and pyzmail modules
#pip install imapclient
#pip install pyzmail

import imapclient, pyzmail, pprint
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('blakekelley127@gmail.com', 'MY_SECRET_PASSWORD')

print('Email folders')
pprint.pprint(imapObj.list_folders())

print('\nSelecrt Inbox folder')
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Jul-2017'])

print('UID\'s')
print(UIDs)

print('Raw messages')
for uid in UIDs:
    print(imapObj.fetch([uid], ['BODY[]', 'FLAGS']))

print('Emails:')
for uid in UIDs:
    message = pyzmail.PyzMessage.factory(rawMessages[uid]['BODY[]'])
    print('\tSubject: ' + message.get_subject())
    sender = message.get_addresses('from')
    print('\tFrom: ' + sender[0] + '(' + sender[1] + ')')
    recipient = message.get_addresses('to')
    print('\tTo: ' + recipient[0] + '(' + recipient[1] + ')')
    bcc = message.get_addresses('cc')
    print('\tTo: ' + cc[0] + '(' + cc[1] + ')')
    bcc = message.get_addresses('cc')
    print('\tTo: ' + bcc[0] + '(' + bcc[1] + ')')

    if message.text_part != None:
        emailText = message.text_part.get_payload().decode(message.text_part.charset)
        print('Email text: ' + emailText)

    if message.html_part != None:
        emailHTML = message.html_part.get_payload().decode(message.html_part.charset)
        print('Email HTML: ' + emailHTML)

imapObj.logout()
