class Node:
    __slots__='_ele','_next'

    def __init__(self,ele):
        self._ele=ele
        self._next=None

class CircularLL:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def isEmpty(self):
        return self._size==0
    
    def __len__(self):
        return self._size
    
    def display(self):
        if (self.isEmpty()):
            print("The list is empty")
            return
        x=self._head
        while(True):
            print(x._ele,end="")
            x=x._next
            if x==self._head:
                break
            print("",end="->")
        print()
    
    def insertEnd(self,ele):
        new=Node(ele)
        if self.isEmpty():
            self._head=new
            self._tail=new
            self._tail._next=self._head
        else:
            self._tail._next=new
            self._tail=new
            self._tail._next=self._head
        self._size+=1

    def insertBeg(self,ele):
        new=Node(ele)
        if self.isEmpty():
            self._head=new
            self._tail=new
            self._tail._next=self._head
        else:
            new._next=self._head
            self._head=new
            self._tail._next=self._head
        self._size+=1

    def insertPos(self,ele,pos):
        if pos==0 or pos>self._size+1:
            print("Enter a valid position !")
            return
        if pos==1:
            self.insertBeg(ele)
            return
        if pos==self._size+1:
            self.insertEnd(ele)
            return
        new=Node(ele)
        count=1
        x=self._head
        while count<pos-1:
            x=x._next
            count+=1
        new._next=x._next
        x._next=new
        self._size+=1

    def deleteEnd(self):
        if self.isEmpty():
            print("The list is already empty.")
            return
        if self._size==1:
            self._head=None
            self._tail=None
            self._tail._next=None
            self._size-=1
            return
        x=self._head
        while x._next._next!=self._head:
            x=x._next
        print("Deleted Node ",x._next._ele)
        x._next=self._head
        self._tail=x
        self._tail._next=self._head
        self._size-=1

    def deletePos(self,pos):
        if pos<1 or pos >self._size:
            print("Enter a valid position !")
            return
        
        if pos==1:
            if self._size==1:
                print("deleted node: ",self._head._ele)
                self._head=None
                self._tail=None
            else:
                print("deleted node: ",self._head._ele)
                self._tail._next=self._head._next
                self._head=self._head._next
            self._size-=1
            return
        
        if pos==self._size:
            self.deleteEnd()
            return
        
        count=1
        x=self._head
        while (count < pos-1):
            count+=1
            x=x._next
        print("deleted node: ",x._next._ele)
        x._next=x._next._next
        self._size-=1






cll=CircularLL()

cll.insertEnd(1)
cll.insertEnd(2)
cll.insertEnd(3)

cll.insertBeg(0)

cll.insertPos("10",2)

cll.deleteEnd()
cll.deletePos(2)

cll.display()
print(cll.__len__())