x=float(input("Enter the value of x: "))
n=int(input("Enter the no. of terms to be considered: "))
ch=int(input("\n1]Exponential series\n2]Sine series\n3]Cosine series\nEnter the choice: "))
f=1
l=-1
s=0
p=1
w=x*3.14/180
if(ch==1):
    for i in range(1,n):
        f=f*i
        s=(s+((x**i)/f))
    print("e^",x,"=",s)     
elif(ch==2):    
    for i in range(1,n):
        f=f*i
        if(i%2==0):
            continue
        l=l*(-1)
        s=s+(l*(w**i)/f)
    print("sin(",x,")deg =",s)
elif(ch==3):    
    for i in range(1,n):
        f=f*i
        if(i%2!=0):
            continue
        p=p+(l*(w**i)/f)
        l=l*(-1)
    print("cos(",x,")deg =",p)
