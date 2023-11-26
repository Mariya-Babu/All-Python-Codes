import pywhatkit as kit
import datetime

# Set the time for the message (24-hour format)
hour = 11
minute = 21

# Message details
phone_number = "919392265983"  # Replace this with the recipient's phone number
message = "This is a scheduled message!"

# Schedule the message
kit.sendwhatmsg(phone_number, message, hour, minute)
