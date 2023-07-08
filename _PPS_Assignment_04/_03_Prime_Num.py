#for x in range(1,21):
#   i=1
#   s=0
#   while(i<=x):
#       if(x%i==0):
#           s+=1
#       i=i+1
#   if(s==2):
#       print(x)        
n=int(input("Enter the no."))
for i in range(2,n):    
    if (n%i==0):
        print(n,"is not a prime no.")
        break
else:
    print(n," is a prime no.")
       