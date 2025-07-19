class Node:
    __slot__='element','next'
    def __init__(self,ele):
        self.element=ele
        self.next=None
    
class QueuesLinked:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size==0
    
    def enqueue(self,e):
        new=Node(e)
        if self.isEmpty():
            self.front=new
        else:
            self.rear.next=new
        self.rear = new
        self.size+=1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        e=self.front.element
        self.front=self.front.next
        self.size-=1
        if self.isEmpty():
            self.rear =None
        return e
    
    def first(self):
        if self.isEmpty():
            print("queue is empty")
            return
        return self.front.element
    
    def display(self):
        p = self._front
        while p:
            print(p._element,end=' <-- ')
            p = p._next
        print()
