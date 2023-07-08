#Lower case

str="LOWER CASE"
for i in str:
    if (ord(i)>64 and ord(i)<91):
        a=ord(i)
        b=a+32
        i=chr(b)
        print(i,end="")
    else:
        print(i,end="")
        