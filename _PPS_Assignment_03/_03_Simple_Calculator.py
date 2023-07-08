# To form a simple calculator

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
print("Chose the operation number:")
print("1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Tangent 6.logarithm 7.Square root")
import math
c = input("Enter operation number:")
if (c=="1"):
    print("Addition-",a+b)
if (c=="2"):
    print("Subtraction-",a-b)
if (c=="3"):
    print("Multiplication-",a*b)
if (c=="4"):
    print("Division-",a/b)
if (c=="5"):
    print(math.tan(a))
    print(math.tan(b))
if (c=="6"):
    print(math.log(a))
    print(math.log(b))
if (c=="7"):
    print(math.sqrt(a))
    print(math.sqrt(b))                       
     
