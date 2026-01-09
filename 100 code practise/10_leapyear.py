
# to check leap year or not
year=int(input("enter year here:"))

if (year%400==0) and (year%100==0):
    print(year," is leap year and  century year")

elif (year%4==0)and(year%100!=0):
    print(year ," is a leap year")

else:
    print(year," is not leap year")    