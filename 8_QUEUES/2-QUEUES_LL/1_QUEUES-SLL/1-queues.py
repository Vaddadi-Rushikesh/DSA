class Node:
    def __init__(self,ele):
        self.ele=ele
        self.next=None

class QueuesLL:
    def __init__(self):
        self.first=None
        self.last=None
        self.size=0

    def isEmpty(self):
        return self.size==0
    
    def __len__(self):
        return self.size
    
    def enqueue(self,ele):
        new = Node(ele)
        if self.isEmpty():
            self.first=new
        else:
            self.last.next=new
        self.last=new
        self.size+=1
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("dequeues element",self.first.ele)
        self.first=self.first.next
        self.size-=1
        if self.isEmpty():
            self.last=None

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        x=self.first
        while x:
            print(x.ele,end=" ")
            x=x.next
        print()
        
q=QueuesLL()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.display()



