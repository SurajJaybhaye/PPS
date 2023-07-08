#Upper case

str="Upper case"
for i in str:
    if (ord(i)>96 and ord(i)<123):
        a=ord(i)
        b=a-32
        i=chr(b)
        print(i,end="")
    else:
        print(i,end="")
        
