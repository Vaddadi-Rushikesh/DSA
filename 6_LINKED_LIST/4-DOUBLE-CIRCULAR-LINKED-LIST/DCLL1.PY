class Node:
    __slot__='ele',"prev","next"
    def __init__(self,ele):
        self.ele=ele
        self.prev=None
        self.next=None
    
l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)

l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l1

l1.prev=l4
l4.prev=l3
l3.prev=l2
l2.prev=l1


print(l1.prev.ele)
