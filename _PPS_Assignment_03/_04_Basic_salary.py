
a = int(input("Basic salary is:"))
if (a>=10000 and a<=20000):
    print("DA on salary is",0.1*a)
elif (a>=20000 and a<=50000):
    print("DA on salary is",0.15*a)
elif (a>=50000 and a<=100000):
    print("DA on salary is",0.2*a)
elif (a>100000):
    print("DA is not apllicable")    
else:
    print("DA is not applicable")
