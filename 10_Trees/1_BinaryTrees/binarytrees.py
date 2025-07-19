from QueuesLinked import QueuesLinked

class Node:
    __slot__='element','left','right'

    def __init__(self,element,left=None,right=None):
        self.element=element
        self.left=left
        self.right=right

class BinaryTrees:
    __slot__='root'

    def __init__(self):
        self.root=None

    def makeTree(self,left,ele,right):
        self.root = Node(ele,left.root,right.root)

    def inorder(self,troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element,end=" ")
            self.inorder(troot.right)

    def preorder(self,troot):
        if troot:
            print(troot.element,end=" ")
            self.preorder(troot.left)
            self.preorder(troot.right)

    def postorder(self,troot):
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.element,end=" ")


    def levelOrder(self):
        Q=QueuesLinked()
        t=self.root
        print(t.element,end=" ")
        Q.enqueue(t)
        while not Q.isEmpty():
            t=Q.dequeue()
            if t.left :
                print(t.left.element,end=" ")
                Q.enqueue(t.left)
            if t.right:
                print(t.right.element,end=" ")
                Q.enqueue(t.right)

    def count(self,troot):
        if troot :
            x = self.count(troot.left)
            y = self.count(troot.right)
            return x+y+1
        return 0


a=BinaryTrees()
b=BinaryTrees()
c=BinaryTrees()
d=BinaryTrees()
e=BinaryTrees()
f=BinaryTrees()
g=BinaryTrees()
h=BinaryTrees()

#                               ex-1
# 
#         1(a)
#       /     \
#    2(b)       3(c)
#    /  \     /    \
# 4(e)  5(f)  6(g)  7(h)

# in-> 4 2 5 1 6 3 7
# pre-> 1 2 3 4 5 3 6 7
# post-> 4 5 2 6 7 3 1
#level-> 1 2 3 4 5 6 7

# e.makeTree(d,4,d)
# f.makeTree(d,5,d)
# g.makeTree(d,6,d)
# h.makeTree(d,7,d) #level 2

# b.makeTree(e,2,f)
# c.makeTree(g,3,h) #level 1

# a.makeTree(b,1,c) #level 0

#                               ex- 2
# d - null reference node
# 
#         10-a
#       /   \
#     20-b    30-c
#   /       / 
# 40-e    50-f
#            \
#             60-g
# Inorder traversal -> 40 20 10 50 60 30 
# Preorder Traversal -> 10 20 40 30 50 60 
# Postorder Traversal -> 40 20 60 50 30 10 
# Level Order Treversal->  10 20 30 40 50 60

g.makeTree(d,60,d) #level-3

e.makeTree(d,40,d)
f.makeTree(d,50,g) #level-2

b.makeTree(e,20,d)
c.makeTree(f,30,d) #level-1

a.makeTree(b,10,c) #level-0


print("Inorder traversal -> ",end="")
a.inorder(a.root)
print()
print("Preorder Traversal -> ",end="")
a.preorder(a.root)
print()
print("Postorder Traversal -> ",end="")
a.postorder(a.root)
print()
print("Level Order Treversal-> ",end=" ")
a.levelOrder()
print()
print("Number of nodes ->",end=" ")
print(a.count(a.root))