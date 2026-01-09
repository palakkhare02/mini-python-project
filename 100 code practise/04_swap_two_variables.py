# using temp variable
a=2
b=3
temp=0
print("Before swapping:")
print("Value of a,b",a ,b)

print("After swapping:")
temp=a
a=b
b=temp
print("Value of a,b",a ,b)

print("______________________")

# without using temp variable

x,y=13,12

print("Before swapping:")
print("Value of x and y is:",x,y)
x,y=y,x
print("After swapping:")
print("Value of x and y is:",x,y)