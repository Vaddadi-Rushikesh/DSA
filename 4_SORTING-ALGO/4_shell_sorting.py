def shellsort(a):
    n=len(a)
    gap=n//2
    while(gap>0):
        i=gap
        while(i<n):
            temp=a[i]
            j=i-gap
            while j>=0 and a[j]>temp:
                a[j+gap]=a[j]
                j=j-gap
            a[j+gap]=temp
            i=i+1
        gap=gap//2

a=[1,42,5,7,4,2]
print("original array: ",a)
shellsort(a)
print("Sorted array: ",a)

#-------------------x--------------------
#geeksForGeeks--practice

def shellsort(a):
    n=len(a)
    gap=n//2
    while(gap>0):
        j=gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j<n:
            i=j-gap
            #this will keep help in maintain gap value
            while i>=0:
                #if value on right side is already greater than left side value
                #we dont do swap else we swap
                if a[i+gap] > a[i]:
                    break
                else:
                    a[i+gap],a[i]=a[i],a[i+gap]
                i=i-gap
                #to check left side also
                #if the element present is greater than current element

            j=j+1
        gap=gap//2

a=[1,42,5,7,4,2]
print("original array: ",a)
shellsort(a)
print("Sorted array: ",a)