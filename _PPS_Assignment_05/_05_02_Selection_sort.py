# Selection sort

a = [74,87,34,65,5]
n=len(a)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if a[j]<a[min]:
            min=j
    temp=a[i]
    a[i]=a[min]
    a[min]=temp
    print(a)  
              