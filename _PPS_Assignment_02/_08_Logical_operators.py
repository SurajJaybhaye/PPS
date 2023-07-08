# Write a program to perform all logical operations

# Logical  Operators

a = int(input("Enter the first no:"))
b = int(input("Enter the second no:"))

p = (a%2==0)
q = (b%2==0)

print("Both are even",p and q)
print("Atleast one is even",p or q)
print("First no. is odd",not p)