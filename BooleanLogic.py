#simple user login system to check how boolean logic works
#get the username and password
username = raw_input("Enter your username")
password = raw_input(("Enter your password"))
if username =="admin":
    if password == "admin123":
        print("Access Allowed")

#Alternative using boolean logic
if username =="admin" and password == "admin123":
    print("Access Allowed")
else:
    print("Invalid User")

#Boolean Operator OR
if username =="admin" or password == "admin123":
    print("Access Allowed")
else:
    print("Invalid User")
