# To find product of digit of no.
n=int(input("Enter the number: "))
p = 1
while(n!=0):
    r = n%10
    n = n//10
    if (r==0):
        continue
    p=p*r
print("Product of it's digit is: ",p) 
