print("Welcome to the Password Validation Tool.\n")
print(""" These are the password requirements:
• A password must have at least eight characters.
• A password consists of only letters and digits.
• A password must contain at least two digits.
""")

user_pwd = input("Enter a password to validate or type the word 'EXIT' to terminate.\n")

while user_pwd.upper() != 'EXIT':
    if len(user_pwd) < 8: #checking length of password.
        print("Invalid Password: A password must have at least eight characters.\n")
    elif (user_pwd.isalnum()) == False:  #determine is password is alphanumeric.
        print("Invalid Password: A password consists of only letters and digits.\n")
    elif sum(c.isdigit() for c in  user_pwd ) < 2: #find out if there are atleast two digits.
        print("Invalid Password: A password must contain at least two digits.")
    else:
        print("Congratulations, you have entered a valid password!\n")
        
    user_pwd = input("Enter another password to validate or 'EXIT' to terminate.\n")
    
print("The keyword 'EXIT' was entered; The program was terminated.")
    


