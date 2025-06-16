def bubbleSort(a):
    n=len(a)
    for i in range(n-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

def rBubbleSort(a):
    n=len(a)
    for i in range(n-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

b=[33,4,6,2,66,1]
bubbleSort(b)
print(b)
rBubbleSort(b)
print(b)
