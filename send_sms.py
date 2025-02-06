from twilio.rest import Client

# Twilio Credentials (Hardcoded - Not Recommended)
ACCOUNT_SID = "ACd3877f49f79adc3d81c7d3a120a41263"
AUTH_TOKEN = "e46a4de560509bd9e2588d537a927a23"
FROM_NUMBER = "+15073535376"  # Your Twilio Number
TO_NUMBER = "+966509640181"  # Replace with the recipient's number
MESSAGE = "Hello! This is a test SMS from GitHub using Twilio."

# Initialize Twilio Client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Send SMS
message = client.messages.create(
    body=MESSAGE,
    from_=FROM_NUMBER,
    to=TO_NUMBER
)

print(f"✅ SMS Sent! Message SID: {message.sid}")
