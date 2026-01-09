#using cmath module (complex math) to solve quadratic equation
# quadratic equation formula ax**2 + bx + c =0
# a,b,c are realnumbers
# a!=0

import cmath

a=int(input("Enter number(a!=0):"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))

# formula for discriminant
d=(b**2)-(4*a*c)

root1= (-b-cmath.sqrt(d))/(2*a)
root2= (-b+cmath.sqrt(d))/(2*a)

print("the roots are ",root1 , "and",root2)