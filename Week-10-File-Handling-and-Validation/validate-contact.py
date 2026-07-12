import re

phone = input("Enter phone number: ")
email = input("Enter email id: ")

phone_pattern = r"^[6-9][0-9]{9}$"
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(phone_pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

if re.match(email_pattern, email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")
