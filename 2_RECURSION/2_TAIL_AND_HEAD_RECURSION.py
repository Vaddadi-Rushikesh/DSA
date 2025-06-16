#head-recursion
def headRecursion(a):
    
    if(a>0):
        print(a**2)
        headRecursion(a-1)

def tailRecursion(a):
    if(a>0):
        tailRecursion(a-1)
        print(a**2)
a =5
print("this is head recusion")
headRecursion(a)
print("")
print("this is tail recusion")
tailRecursion(a)
# tail and head recursion
# tail and head recursion