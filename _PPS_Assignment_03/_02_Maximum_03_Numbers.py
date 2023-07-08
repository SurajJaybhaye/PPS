# Maximum number amongst 3 numbers
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if (a>=b and a>=c):
     print(a,"is maximum number")  
elif (b>=c):
     print(b,"is maximum number")
else:
     print(c,"is maximum number") 