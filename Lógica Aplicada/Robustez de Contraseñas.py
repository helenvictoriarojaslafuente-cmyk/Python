password = input("Enter your password: ")
if len(password) < 8 and "clave" not in password and "123" not in password:
    print("Secure password")
else:
    print("Insecure password")