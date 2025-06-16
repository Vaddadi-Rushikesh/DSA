#using iteration function --------------------X------------------------

def binSearchIter(a,key):
    ind=0
    l=len(a)
    z=l-1
    while(ind<=z):
        m=(ind+z)//2
        if (key==a[m]):
            return m
        elif(key<a[m]):
            z=m-1
        elif(key>a[m]):
            ind=m+1
    return -1


a=[1,4,5,2,3,6,7,8,9]
a.sort()
print("position",binSearchIter(a,8))

#using recursive functions--------------------X------------------------

def binSearchRec(a,key,l,r):
    if l>r:
        return -1
    else :
        m=(l+r)//2
        if(a[m]==key):
            return [m+1]
        elif a[m]>key:
            return binSearchRec(a,key,l,m-1)
        else:
            return binSearchRec(a,key,m+1,r)


a=[1,4,5,2,3,6,7,8,9]
a.sort()
l=len(a)
print("position",binSearchRec(a,6,0,l-1))