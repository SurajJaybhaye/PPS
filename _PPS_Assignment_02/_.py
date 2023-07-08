n=int(input("Enter the number: "))
p = 1
i = 0
while(n!=0):
    r = n%10
    p=p*r
    n = n//10
    i=i+1
print('Product of it\'s digit is: ',p)
    