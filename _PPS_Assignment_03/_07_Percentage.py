a = float(input("Enter marks of first subject: "))
b = float(input("Enter marks of second subject: "))
c = float(input("Enter marks of third subject: "))
d = float(input("Enter marks of fourth subject: "))
e = float(input("Enter marks of fifth subject: "))

f = ((a+b+c+d+e)/500)*100
print("Percentage",f,"%")
if (f>=60):
    print("First Division")
elif (f>=50 and f<=59):
    print("Second Division")
elif (f>=40 and f<=49):
    print("Third Division")
else:
    print("Fail")             