class _Node:
    __slots__= '_prev','_ele','_next'

    def __init__(self,ele):
        self._prev = None
        self._ele = ele
        self._next = None


d0 = _Node(56)
d1 = _Node(57)
d2 = _Node(58)

d0._next = d1
d1._next =d2

d2._prev = d1
d1._prev = d0


head = d0
tail=None
x=head
while (True):
    print(x._ele,end=" ")
    if x._next is None:
        tail = x
        break
    x=x._next


    
