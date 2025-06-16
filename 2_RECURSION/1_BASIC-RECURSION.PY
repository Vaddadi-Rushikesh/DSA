def calculate (a):
    if(a>0):
        
        calculate(a-1)
        print(a**3)
    else:
        return

a = int(input("enter a number: "))
calculate(a)
print("")

#iteration
while(a!=0):
    print(a**3)
    a=a-1