# Write a program for conversion of units

F = float(input("Enter the temperature in Fahrenhite is: "))
C = ((F-32)*5)/9
print("The temperature in Celsius is",C)

C = float(input("Enter the temperature in Celsius is: "))
F = (C*9/5)+32
print("The temperature in Fahrenhite is",F)