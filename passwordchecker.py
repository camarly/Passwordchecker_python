
isvalid = False #declare iterator value

print("Welcome to the Password Validator \n") #Welcome message

while not (isvalid):   #loop
   
   user_pwd = input("Please enter your password \n") #get password
   
   print("Validating Password..") #indicator message
   
   print(" ...")
   
   def pwd_ValTool(password): #func to validate password
      if len( password ) < 8: #length of password
         print("Invalid Password: A password must have at least eight characters.")
      elif password .isalnum() == False: #determine is password is alphanumeric
          print("Invalid Password: A password consists of only letters and digits.")
      elif sum(c.isdigit() for c in  password ) < 2: #find out if there are atleast two digits.
         print("password must contain at least two digits.")
      else:
         print("password is valid.")
         return True
      
      return False #end loop
   
   isvalid = pwd_ValTool(user_pwd)
