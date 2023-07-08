def power():
    base=int(input("enter the base: "))
    exp=int(input("Enter exponentional: "))
    work(base,exp)
    print(work(base,exp))
def work(base,exp):
    if exp==0:
        return 1
    else:
        return base*work(base,exp-1)
power()   

 
