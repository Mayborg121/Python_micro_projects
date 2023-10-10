#a-z
#0-9
#. _ 
#@ 1 time
#. 2,3
import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" 
user_email=input('Enter your E-Mail : ')

if re.search(email_condition,user_email):
    print("\n*** Valid Email !!! ***\n")
    
else:
    print('\n***   Invalid E-mail !!!   ***\n')