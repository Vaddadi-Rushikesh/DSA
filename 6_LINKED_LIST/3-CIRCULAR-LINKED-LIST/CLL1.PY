class Node:
    __slots__='_next','_ele'

    def __init__(self,ele):
        self._ele=ele
        self._next=None

l1=Node(1)
l2=Node(2)
l3=Node(3)
l4=Node(4)
l5=Node(5)

l1._next=l2
l2._next=l3
l3._next=l4
l4._next=l5
l5._next=l1
#---------------l1->l1->l3->l1->.....

head=l1
# print(head._next._ele)
x=head
tail=None
while True:
    print(x._ele)
    tail=x
    x=x._next
    if(x._next==head):
        tail=x
        print(x._ele)
        break

print("tail",tail._ele)