#! python3
# sendEmail.py - 

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

print('Enter Email adress:')
emailaddr = input()

print('Enter password')
password = input()

mtpObj.login(emailaddr, password)

print('To Email address')
recipientaddr = input()

print('Enter the subject')
subject = input()

print('Enter Email body')
body = input()

emailText = 'Subject ' + subject + '\n' + body)
smtpObj.sendmail(emailaddr, recipientaddr,emailText)

smtpObj.quit()
