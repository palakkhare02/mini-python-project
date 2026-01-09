x=int(input("enter number 1:"))
y=int(input("enter number 2:"))
z=int(input("enter number 3:"))

if(x>y):
    if(x>z):
        print(x," is greatest number among three numbers")

    else:
        print(z," is greatest")    
else:
    print(y,"is greatest")        


# using and operator
if(x>y) and (x>z):
    print(x,"is greatest number")
elif(y>x)and(z>y):
    print(y,"is greatest number") 
else:
    print(z,"is greatest number ")          