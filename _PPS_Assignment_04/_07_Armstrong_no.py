n = int(input("Enter tje no: "))
p = 0
num = n
while(n!=0):
    r=n%10
    p=p+r**3
    n=n//10
if(p==num):
    print(num,"is an Armstrong no.")
else:
    print(num,"is not an Armstrong no.")        
    