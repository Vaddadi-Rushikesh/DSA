def linearSearch(a,key):
    length= int(len(a))
    index=0

    while(index<length):
        if a[index]==key:
            return index+1
        index=index+1
    return -1
        

a=[1,4,5,2,3,6,7,8,9]

print("position -",linearSearch(a,9))
