# first_name = input("What is your name?")
# last_name = input("What is your last name?")

# length = len(first_name)
# length2 = len(last_name)
# if length >= 2 and length2 >= 2:
#     print("Great going")
# else:
#     print("Error message")
    
    



def password():
    password_use = input("Password?")
    password_capital = password_use.upper()
    password_lower = password_use.lower()
    if password_use != password_capital and password_use != password_lower and len(password_use) >= 8:
        print("Ok")
    else:
        print("Password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number.")



password()
    