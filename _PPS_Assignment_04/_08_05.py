c=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
n=0
for i in range(5):
    for j in range(i+1):
        print(c[n],end=" ")
        n = n+1 
    print()    