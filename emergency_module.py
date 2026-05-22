import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

SAFE_WORD = "order pizza"

# Twilio credentials from environment variables
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
EMERGENCY_CONTACT = os.getenv("EMERGENCY_CONTACT")

def trigger_emergency(location="0,0"):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=f"""🚨 EMERGENCY ALERT
User triggered safe word.
Location:
https://www.google.com/maps?q={location}
""",
            from_=TWILIO_NUMBER,
            to=EMERGENCY_CONTACT
        )
        print("SMS Sent:", message.sid)
    except Exception as e:
        print("Error sending SMS:", e)