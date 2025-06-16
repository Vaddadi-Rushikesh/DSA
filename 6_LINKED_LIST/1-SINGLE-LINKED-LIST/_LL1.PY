#Linked list creation lecture -1

class Node:
    __slots__='_ele','_next'

    def __init__(self,ele,next):
        self._ele = ele
        self._next = next

n1 = Node(1,None)
n2 = Node(5,None)
n3 = Node(2,None)
n4 = Node(4,None)

n1._next = n3
n3._next = n4
n4._next = n2

head = n1
x=head
# print(n1._ele,n2._ele,n3._ele)
tail = None

print("The linked list is : ",end=" ")
while(True):
    print(x._ele,end=" ")
    if(x._next==None):
        tail=x
        print()
        break
    print("",end="-> ")
    x=x._next

print("The head element is :",head._ele)
print("The tail element is :",tail._ele)
