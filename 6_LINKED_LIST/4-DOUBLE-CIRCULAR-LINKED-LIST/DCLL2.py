class Node:
    __slot__='ele','prev','next'
    def __init__(self,ele):
        self.ele=ele
        self.prev = None
        self.next = None
    
class DCLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def isEmpty(self):
        return self.size==0
    
    def __len__(self):
        return self.size
    
    def display(self):
        if self.size==0:
            print("List is empty !")
            return
        x=self.head
        for _ in range(self.size):
            print(x.ele,end=" <-> ")
            x=x.next
        print()
    
    def addPos(self,ele,pos):
        if pos <1 or pos >self.size+1:
            print("enter a valid position ")
            return
        new = Node(ele)
        if pos==1:
            if self.isEmpty():
                self.head = new
                self.tail=new
                new.next=new
                new.prev=new
            else:
                new.next=self.head
                new.prev=self.tail
                self.tail.next=new
                self.head.prev=new
                self.head=new
                # return
        elif pos == self.size+1:  
            new.next=self.head
            new.prev=self.tail
            self.head.prev=new
            self.tail.next=new
            self.tail=new
        else:
            x=self.head
            count=1
            while count < pos-1:
                x=x.next
                count+=1
            new.next=x.next
            new.prev=x
            x.next.prev=new
            x.next=new
        self.size+=1
            
    def delPos(self,pos):
        if self.isEmpty():
            print("List is empty !")
            return
        if pos<1 or pos>self.size:
            print("Invalid pos !")
            return
        if pos==1:
            if self.size==1:
                print("deleted element",self.head.ele)
                self.head=None
                self.tail=None
            else:
                print("deleted element",self.head.ele)
                self.tail.next=self.head.next
                self.head.next.prev=self.tail
                self.head=self.head.next
        elif pos == self.size:
            print("deleted element",self.tail.ele)
            self.tail.prev.next=self.head
            self.head.prev=self.tail.prev
            self.tail=self.tail.prev
        else:
            x=self.head
            count=1
            while count<pos:
                x=x.next
                count+=1
            print("deleted element",x.ele)
            x.prev.next=x.next
            x.next.prev=x.prev
        self.size-=1


L = DCLL()
L.addPos(1,1)
L.addPos(2,2)
L.addPos(3,3)
L.addPos(0,1)
L.addPos(101,1)
L.addPos(5,5)
L.display()

L.delPos(1)
L.delPos(4)
L.display()
