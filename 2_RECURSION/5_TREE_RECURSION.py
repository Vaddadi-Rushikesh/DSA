def treeRecursion(a):
    if(a>0):
        treeRecursion(a-1)
        print(a)
        treeRecursion(a-1)

a=3
treeRecursion(a)