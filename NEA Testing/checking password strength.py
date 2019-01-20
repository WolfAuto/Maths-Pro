import string
from tkinter import messagebox

 def length_check(password):
     "Password must be at least 8 characters long"
    return len(password) >= 8

def lowercase_check(password):
    "Password must contain a lowercase character"
    return len(set(string.ascii_lowercase).intersection(password)) > 0

def uppercase_check(password):
    "Password must contain a uppercase character"
    return len(set(string.ascii_uppercase).intersection(password)) > 0

def numeric_check(password):
    "Password must contain a digit"
    return len(set(string.digits).intersection(password)) > 0

def special_check(password):
    "Password must conatin a special character"
    return len(set(string.punctuation).intersection(password)) > 0

def test_password(password, tests=[length_check, lowercase_check, uppercase_check,
                                       numeric_check, special_check]):
    for test in tests:
        if not test(password):
            messagebox.showwarning("Password", test.__doc__)
            return False
    return True


def main():
    pw = input('Please enter a test password:')
    if test_password(pw):
        print('That is a good password!')


if __name__ == "__main__":
    main()
