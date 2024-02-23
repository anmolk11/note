from twilio.rest import Client
import os
from dotenv import load_dotenv
import pyotp

load_dotenv()
secret_key = pyotp.random_base32()
totp = pyotp.TOTP(secret_key,interval=60)

def send_otp() -> bool:
  account_sid = os.getenv("account_sid")
  auth_token =  os.getenv("auth_token")

  secret_key = pyotp.random_base32()
  totp = pyotp.TOTP(secret_key,interval=60)
  otp = totp.now()

  try:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
      from_='+16505819194',
      body=f'Your otp is {otp}',
      to='+917415227505'
  )
  except Exception as e:
    print('Exception occured',e)
    return False
  
  return True


def verify_otp(otp : str) -> bool:
  return totp.verify(otp)


if __name__ == '__main__':
  pass