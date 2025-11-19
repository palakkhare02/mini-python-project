#email validation using string example-palak1902@gmail.com
email=input("enter your email :")
k,j,d=0,0,0

if len(email)>=6:

    #check the condition of letter of email should alphabet character
    if email[0].isalpha():

        # to check the @ in the gmail or string(using membership operator)
        if ("@" in email) and (email.count("@")==1):
          
        # to check the (.)dot position in email
          if (email[-4]==".")^ (email[-3]=="."):
                
                #to check space in email
                for i in email:
                    if i==i.isspace():
                        k=1  #k for space
                    #to check alphabet ,digit , capital letter and special character in email 
                    elif i.isalpha():
                        if i.isupper():
                            j=1  # j use for capital letter
                    elif i.isdigit():
                       continue
                    elif i=="." or i=="_" or i=="@":  
                        continue
                    else:
                        d=1       # d use for special character
                if k==1 or j==1 or d==1:
                    print("Wrong email due to 5 ")
          else:
            print("Wrong Email due to 4 conditon") 
             
        else:
            print("Wrong Email due to 3 condition")
    else:
        print("Wrong Email due to 2 condition")
else:
    print("wrong Email Due to 1 condition")