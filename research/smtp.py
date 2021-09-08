import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import login as l

mail_content = "Hello This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library"
#The mail addresses and password
sender_address = l.sender_email #sender_address = 'sender123@gmail.com' 
sender_pass = l.sender_pass #sender_pass = 'xxxxxxxx' 
receiver_address = l.receiver_email #receiver_address = 'receiver567@gmail.com' 

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')