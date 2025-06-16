def selectionsort(a,l):
    for i in range(l):
        pos=i
        for j in range(i+1,l):
            if a[j]<a[pos]:
                pos=j
        temp = a[i]
        a[i]= a[pos]
        a[pos]=temp
    return a

a=[1,4,5,7,8,9]
print(selectionsort(a,len(a)))

#practice-------------------------x---------------------------

def selectionsort(a):
    n=len(a)
    for i in range(n):
        pos=i
        for j in range(i+1,n):
            if a[j]<a[pos]:
                pos=j
        a[i],a[pos]=a[pos],a[i]

a=[1,4,5,7,8,2,3]
selectionsort(a)
print(a)

#------------selection sorting in desc order--------------

def rSelectionSort(a):
    n=len(a)
    for i in range(n):
        pos=i
        for j in range(i+1,n):
            if a[j]>a[pos]:
                pos=j
        a[i],a[pos]=a[pos],a[i]

a=[1,4,5,7,8,2,3]
rSelectionSort(a)
print(a)