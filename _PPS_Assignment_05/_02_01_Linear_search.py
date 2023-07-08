# Linear Search

a=[4,69,3,89,43]
x=int(input("Enter the no. to be search: "))
for i in range(len(a)):
    if a[i]==x:
        print("No. search at index: ",i)
        break
else:
    print("No. is not present in given array")