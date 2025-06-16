def sum(a):
    count=a
    if(a>0):
        count=count+sum(a-1)

    return count
        

print(sum(10))