def quickSort(a, low, high):
    if low < high :
        pi = partition(a,low,high)
        quickSort(a, low,pi-1)
        quickSort(a, pi+1,high)

def partition(a, low, high):
    pivot=a[low]
    i=low+1
    j=high

    while True:
        while i<=j and a[i]<=pivot:
            i=i+1
        while i<=j and a[j]>pivot:
            j=j-1
        if i<=j:
            a[i],a[j]=a[j],a[i]
        else:
            break
    a[low],a[j]=a[j],a[low]
    return j

a=[3,1,5,2,6,4,9,8,7]
quickSort(a,0,len(a)-1)
print(a)

#------------practice----------


# def quickSort(a,low,high):
#     if low<high:
#         pi= partition(a,low,high)
#         quickSort(a,low,pi-1)
#         quickSort(a,pi+1,high)

# def partition(a,low,high):
#     pivot = a[low]
#     i=low+1
#     j=high

#     while True:
#         while i<=j and a[i]<=pivot:
#             i=i+1
#         while i<=j and a[j]>pivot:
#             j=j-1
#         if i<=j:
#             a[i],a[j]=a[j],a[i]
#         else:
#             break
#     a[low],a[j]=a[j],a[low]
#     return j
    
# a=[1,4,2,5,3,7,6]
# quickSort(a,0,len(a)-1)
# print(a)