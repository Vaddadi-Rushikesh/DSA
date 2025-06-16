def insertionSort(a):
    n = len(a)
    for i in range(1,n):
        temp= a[i]
        pos = i-1
        while pos>=0 and a[pos]>temp:
            a[pos+1]= a[pos]
            pos=pos-1
        a[pos+1]=temp

a=[23,11,3,5,66,444,4]
print("original list:",a)
insertionSort(a)
print("sorted list:",a)

#-----practice-------------------

def insertionSort(a):
    n=len(a)
    for i in range(1,n):
        temp=a[i]
        pos=i-1
        while pos>=0 and a[pos]>temp:
            a[pos+1]=a[pos]
            pos=pos-1
        a[pos+1]= temp

def rInsertionSort(a):
    n= len(a)
    for i in range(1,n):
        temp=a[i]
        pos=i-1
        while pos>=0 and a[pos]<temp:
            a[pos+1]=a[pos]
            pos=pos-1
        a[pos+1]=temp

a=[23,11,3,5,66,444,4]
rInsertionSort(a)
print(a)
