class Node:
    __slot__='ele','next'
    def __init__(self,ele):
        self.ele=ele
        self.next=None
    
class StackLL:
    def __init__(self):
        self.top=None
        self.size=0
    
    def isEmpty(self):
        return self.size==0
    
    def push(self,ele):
        new = Node(ele)
        if self.isEmpty():
            self.top=new
        else:
            new.next=self.top
            self.top=new
        self.size+=1

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return
        else:
            print("popped element",self.top.ele)
            self.top=self.top.next
            self.size-=1
            return
    def topele(self):
        if self.isEmpty():
            print("stack is empty")
            return
        print("top element",self.top.ele)
        return
    
    def display(self):
        if self.isEmpty():
            print("stack is empty")
            return
        x=self.top
        while x!=None:
            print(x.ele,end=" ")
            x=x.next
        print()


s=StackLL()

s.push(1)
s.push(2)
s.push(3)
s.pop()
s.display()
s.topele()
