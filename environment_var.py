import os
import smtplib

os.environ["email_user"] = 'mitchbrownuw@gmail.com'
os.environ["user_pass"] = 'yeioupexaylbgggj'

email_address = os.environ.get('email_user')
email_password = os.environ.get('user_pass')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()         # identifies ourselves with the mail server
    smtp.starttls()     # encrypt our traffic
    smtp.ehlo()         # reidentify as an encrypted connection
    
    smtp.login(email_address, email_password)        # log into our mail server
    
    subject = 'Grab dinner this weekend?'
    body = 'how about dinner at 6pm this Saturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email_address, 'mitchbrownuw@gmail.com', msg)