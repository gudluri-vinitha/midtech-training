username = input("Enter username: ")
password = input("Enter password: ")

if len(password) < 8:
    print("Password must be at least 8 characters.")
elif "@" in password or "#" in password or "$" in password or "*" in password:
    print("Login Successful")
else:
    print("Password must contain a special character.")