def mergeSort(a,left,right):
    if left<right:
        mid=(left+right)//2
        mergeSort(a,left,mid)
        mergeSort(a,mid+1,right)
        merge(a,left,mid,right)

def merge(a,left,mid,right):
    i=left
    j=mid+1
    k=left
    b=[0]*(right+1)
    while i<=mid and j<=right:
        if a[i]<a[j]:
            b[k]=a[i]
            i=i+1
        else:
            b[k]=a[j]
            j=j+1
        k=k+1
    while i<=mid:
        b[k]=a[i]
        i=i+1
        k=k+1
    while j<=right:
        b[k]=a[j]
        k=k+1
        j=j+1

    for x in range(left,right+1):
        a[x]=b[x]

a=[1,5,2,7,3,8,4]
print("Original list:",a)
mergeSort(a,0,len(a)-1)
print("Sorted list: ",a)