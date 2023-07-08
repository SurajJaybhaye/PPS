#a=[4,6,2,65,6,65]
#a.sort()
#print(a[a.index(max(a))-1])   

#a=[4,65,3,6,7,65,65,33,2]
#seg=int(input("e"))
#n=int(input("n"))
#d=len(a)//seg
#flag=0
#for i in range(d):
#    for j in range(i*seg,(i+1)*seg):
#        if a[j]==n:
#            flag+=1
#            break
#if flag==seg:
#    print("yes")
#else:
#    print("n")          

#a=[3,6,7,4,43]
#b=[5,6,7,8,43,3]
#c=[]
#d=[]
#for i in range(len(a)): 
#    for j in range(len(b)):
#        if a[i]==b[j]:
#            c.append(a[i])
#print(c)
l=[]
n=int(input("Enter the no: "))
for i in range(n+1):
    p=0
    f=0
    while(i!=0):
        r=i%2
        p=p+r*(10**f)
        i=i//2
        f+=1
    l.append(p)
print(l) 


 

