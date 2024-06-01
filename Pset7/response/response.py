from validators import email

if email(input("Email: ")):
    print("Valid")
else:
    print("Invalid")
