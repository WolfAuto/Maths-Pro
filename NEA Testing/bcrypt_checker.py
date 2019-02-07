import bcrypt

def bcryptchecker():
    password = input("Enter your password")
    hashed = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
    print(hashed)
    print(len(hashed))

bcryptchecker()
