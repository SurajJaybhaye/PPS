# Insertion sort

a = [77,66,55,44,33,22]
n=len(a)
for i in range(1,n):
    key=a[i]
    j=i-1
    while(j>=0 and a[j]>key):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=key
    print(a)  
           