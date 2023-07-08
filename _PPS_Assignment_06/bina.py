def binary_to_decimal(a):
    if a==0:
        return 0
    else:
        return a%10+2*binary_to_decimal(a//10) 
a = int(input("Enter the number "))
print(" Decimal to binary",binary_to_decimal(a)) 