import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import pyotp

load_dotenv()
secret_key = pyotp.random_base32()
totp = pyotp.TOTP(secret_key,interval=60)

def send_email_otp(email : str):
    sender_email = "anmol.anmolkhandelwal@gmail.com"  
    sender_password = os.getenv("app_password")  

    secret_key = pyotp.random_base32()
    totp = pyotp.TOTP(secret_key,interval=60)
    otp = totp.now()

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = 'OTP For myNote'

    message = f'Your One Time Password is {otp}, valid for 1 minute.'
    
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)  
    server.starttls()  
    server.login(sender_email, sender_password)

    server.sendmail(sender_email, email, msg.as_string())

    server.quit()

def verify_otp(otp : str) -> bool:
  return totp.verify(otp)

if __name__ == '__main__':
    email = "akcp.cpp@gmail.com"
    send_email_otp(email)