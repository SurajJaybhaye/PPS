# Bubble sort

a = [77,66,55,44,33,22]
n=len(a)
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            print(a)
