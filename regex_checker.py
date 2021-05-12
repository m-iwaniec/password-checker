import re

password = input("Enter password to test: ")
if not re.search('[A-Z]', password):
    print("Your password is not safe! It needs at least one uppercase letter!")
else:
    if not re.search('[a-z]', password):
        print("Your password is not safe! It needs at least one lowercase letter!")
    else:
        if not re.search('[0-9]', password):
            print("Your password is not safe! It needs at least one number!")
        else:
            if not re.search('[@#$%^*&<>~!/+=]', password):
                print("Your password is not safe! It needs at least one special character!")
            else:
                if re.fullmatch('[A-Za-z0-9@#$%^*&<>~!/+=]{8,16}', password):
                    print("Your password is safe!")
                else:
                    print("Your password needs to be between 8-16 characters long!")

