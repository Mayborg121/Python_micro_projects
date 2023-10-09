print("\n")
email=input("Enter your E-mail : ")
k,j,d=0,0,0

if  len(email)>=6 :#1 m@m.in
    
    if email[0].isalpha():#2
        
        if ("@" in email) and (email.count("@")==1) :#3
            
            if (email[-4]==".") ^ (email[-3]=="."):#4
                
                for i in email :
                    
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1     
                    elif i.isdigit():
                        continue   
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1           
                if k==1 or j==1 or d==1:
                    print("\n")
                    print("Invalid E-mail, Error[5] : Use of Invalid Characters !!!")    
                    print("\n")
                else:
                    print("\n")
                    print("*** Your E-mail is Valid *** ")
                    print("\n")
            else:
                print("\n")
                print('Invalid E-mail, Error[1] : "." is Not present or Misposition !!!')
                print("\n")
        else:
            print("\n")
            print("Invalid E-mail, Error[3] : @ symbol Repeated or Missing !!!")
            print("\n")
    else:
        print("\n")
        print("Invalid E-mail, Error[2] : First letter Must be Lower Case !!!")
        print("\n")
else :
    print("\n")
    print("Invalid E-mail Address, Error[1] : E-mail too Short !!!")
    print("\n")