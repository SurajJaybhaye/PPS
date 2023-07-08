#Binary Search 

a=[4,69,83,95,6,9]
x=int(input("Enter the no. to be search: "))
n=len(a)
start=0
end=n-1
mid=0
flag=0
a.sort()
while start<=end:
    mid=(start+end)//2
    if a[mid]==x:
        i=mid
        flag=1
        break
    elif a[mid]<x:
        start=mid+1
    elif a[mid]>x:
        start=mid-1
if flag==1:
    print("No.is found at index: ",i) 
else:
    print("No. is not in given array")
    