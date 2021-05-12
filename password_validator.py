def validate():
    password = input("Enter your password to check if it is secure enough.\n")
    if len(password) < 8:
        print("Your password is too short! Enter at least 8 characters! Try again!\n")
        exit()
    else:
        if not any(c in password for c in ['!', ',', '.', '@', '#', '$', '%', '^', '&', '*', '?', '/', r'\\',
                                           '-', '(', ')', '+', '=', '[', ']']):
            print('You need at least one special character in your password!')
            return False
        if not any(c.isdigit() for c in password):
            print("no digits")
            return False
        if not any(c.islower() for c in password):
            print("Your password needs at least one lowercase letter!")
            return False
        if not any(c.isupper() for c in password):
            print("Your password needs at least one uppercase letter!")
            return False
        print("Your password is secure!")


validate()
