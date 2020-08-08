"""
Using Python to send Email
"""

import smtplib

# server = smtplib.SMTP('smtp.gmail.com', 587)
#
# server.ehlo()
# server.starttls()
# server.ehlo()
#
# my_email  = 'aaa_sample@gmail.com'
# my_password = 'pwdsample'
# target_email =  'her_sample@gmail.com'
#
# server.login(my_email, my_password)
#
# msg = "\n Darling, I love you:)"
#
# server.sendmail(my_email, target_email, msg)
#
# print('done')

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fromaddr = "test_from@gmail.com"
toaddr = "test_to@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python Test email"

body = "Dear Shanshan, I miss you so much! Where are you?"
msg.attach(MIMEText(body, 'plain'))

username = 'sample@gmail.com'
pwd = 'E******a'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, pwd)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

print('Done')