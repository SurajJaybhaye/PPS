n=int(input("Enter the no: "))
i=0 
while (n!=0):
    f=n%10
    i=i*10+f 
    n=n//10  
print(i)        
  