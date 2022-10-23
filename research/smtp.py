import smtplib
from login import *

gmail_user = 'sender email'
gmail_password = 'sender pwd'
r_user = 'receiver email'

sent_from = gmail_user
to = [r_user]
subject = 'UAT Test'
body = 'Hey, whats up'

email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:
    print ('Something went wrong...again')
