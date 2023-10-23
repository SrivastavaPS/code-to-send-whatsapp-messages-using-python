import pywhatkit

# Get contact number and message from the user
contact_number = input("Enter contact number to whom to send the message: ")
message = input("\nEnter message to send: ")

# Send the message at a specific time (e.g., 10:37 AM)
pywhatkit.sendwhatmsg(contact_number, message, 10, 37)
