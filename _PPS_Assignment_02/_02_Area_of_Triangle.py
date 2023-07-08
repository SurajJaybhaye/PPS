#  Write a program to find area of triangle using Heron's formula

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

s=(a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("The area of triangle is",area)



