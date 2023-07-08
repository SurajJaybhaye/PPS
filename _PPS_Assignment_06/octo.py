a = int(input("Enter the binary "))
octaldigit = 0
ocatalnum =[]
i = 0
mul = 1
chk = 1
while (a !=0):
    rem = a%10
    octaldigit = octaldigit + (rem * mul)
    if chk % 3==0 :
        ocatalnum.insert(i, octaldigit)
        mul = 1
        octaldigit = 0
        chk = 1
        i = i+1
    else:
        mul = mul*2
        chk = chk + 1
    a = int (a/10)
if chk!= 1:
    ocatalnum.insert(i, octaldigit)
print("\n Enter the octate value ", end= "")
while (i>=0):
    print(str(ocatalnum[i]), end ="")
    i = i-1
print()