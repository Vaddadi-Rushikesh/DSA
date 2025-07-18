class Node:
    def __init__(self,ele):
        self.ele=ele
        self.next=None
        self.prev=None

class QueuesDll():
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0

    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size==0
    
    def enqueueRear(self,ele):
        new = Node(ele)
        if(self.isEmpty()):
            self.front=new
            self.rear=new
        else:
            # new.next=self.front
            new.prev=self.rear
            # self.front.prev=new
            self.rear.next=new
            self.rear=new
        self.size+=1

    def enqueueFront(self,ele):
        new=Node(ele)
        if(self.isEmpty()):
            self.front=new
            self.rear=new
        else:
            new.next=self.front
            # new.prev=self.rear
            # self.rear.next=new
            self.front.prev=new
            self.front=new
        self.size+=1
    
    def dequeueRear(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        else:
            print("dequeued element",self.rear.ele)
            if self.size==1:
                self.front=None
                self.rear=None
            else:
                self.rear=self.rear.prev
                self.rear.next=None
        self.size-=1
    
    def dequeueFront(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        else:
            print("dequeued element",self.front.ele)
            if self.size==1:
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
                self.front.prev=None
        self.size-=1

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Queues is :",end=" ")
        x=self.front
        while x:
            print(x.ele,end=" <-> ")
            x=x.next
        print()

q = QueuesDll()
q.enqueueRear(1)    # 1
q.enqueueRear(2)    # 1 -> 2
q.enqueueRear(3)
q.enqueueFront(0)
q.display()

q.dequeueFront()
q.dequeueRear()
q.display()