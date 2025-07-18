class QueuesA:
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data)==0
    
    def enqueue(self,ele):
        self.data.append(ele)

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        print("dequeued element",self.data[0])
        self.data.pop(0)

    def first(self):
        if self.isEmpty():
            print("queue is empty")
            return
        print("first element",self.data[0])

q=QueuesA()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q.data)
q.first()