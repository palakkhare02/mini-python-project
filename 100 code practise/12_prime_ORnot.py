
# # number is prime or not
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# prime number in interval

lower_number=int(input("Enter the lower number here :"))
upper_number=int(input("Enter the upper number here :")) 

for num in range(lower_number,upper_number+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
              
                break
        else:
            print(num)    
