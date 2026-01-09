num1 = int(input("Enter the number for factorial: "))
fact = 1

if num1 < 0:
    print("Factorial is not defined for negative numbers.")
elif num1 == 0 or num1 == 1:
    print(f"Factorial of {num1} is 1")
else:
    for i in range(2, num1 + 1):
        fact *= i
    print(f"Factorial of {num1} is {fact}")
  
# using recursion  


def fact(a):
    if a==0:
        return 1
    else:
        return (a) * fact(a-1)
    
a=int(input("Enter the number for factorial:")) 
print(fact(a))