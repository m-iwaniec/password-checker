import re
password = input("Enter string to test: ")


def low_case():
    if re.search("[a-z]", password):
        up_case()
    else:
        print("Your password needs at least one lowercase letter!")


def up_case():
    if re.search('[A-Z]', password):
        digits()
    else:
        print("Your password needs at least one uppercase letter!")


def digits():
    if re.search('[0-9]', password):
        specials()
    else:
        print("Your password needs at least one digit!")


def specials():
    if re.search('[@#$%!*^&+-.=]', password):
        print("Your password is secure! Good job!")
    else:
        print("Your password needs at least one special character @#$%!-*^&+=")


def check():
    if len(password) < 8:
        print("Your password needs to be at least 8 character long.")
    else:
        low_case()


check()

# re.match ensures string starts with pattern
# re.fullmatch ensures the full string matches the pattern
# re.search ensures the string contains the pattern
