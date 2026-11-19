password = input("enter your pass:")
try:
    
    if len(password) < 8 or not password.isalpha():
        raise ValueError("pass must contain 8 letter  and it should be charachter")
    print("invalid pss")
except ValueError as e :
   print(e)

    
