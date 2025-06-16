def fac(a):
    mul=a
    if(a==0 or a==1):
        return 1
    else:
        return a*fac(a-1)

print(fac(5))