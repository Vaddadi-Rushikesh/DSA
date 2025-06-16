class Node:
    __slots__='_prev','_ele','_next'

    def __init__(self,ele):
        self._prev=None
        self._ele=ele
        self._next=None
    
class DoubleLL:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size==0

    def display(self):
        if self.isEmpty():
            print("the list is empty !")
            return
        x=self._head
        print("the lined list is : ",end="")
        while True:
            print(x._ele, end="")
            if x._next is None:
                print()
                break
            print("",end=" <-> ")
            x=x._next
        

    def insertLast(self,ele):
        new=Node(ele)
        if self.isEmpty():
            self._head=new
            self._tail=new
        else:
            self._tail._next=new
            new._prev=self._tail
            self._tail=new
        self._size+=1

    def insertBeg(self,ele):
        new = Node(ele)
        if self.isEmpty():
            self._head=new
            self._tail=new
        else:
            new._next=self._head
            self._head._prev=new
            self._head=new
        self._size+=1

    def insertPos(self,ele,pos):
        new=Node(ele)
        if pos==0:
            print("enter a valid position !")
            return
        if pos==1:
            self.insertBeg(ele)
            return
        if pos == self._size+1:
            self.insertLast(ele)
            return
        count=1
        x=self._head
        while count < pos-1:
            x=x._next
            count+=1
        new._next=x._next
        new._prev=x
        x._next._prev=new
        x._next=new
        self._size+=1
    
    def deleteLast(self):
        if self.isEmpty():
            print("The lsit is empty !")
            return
        if self._size==1:
            self._head=None
            self._tail=None
        else:
            self._tail=self._tail._prev
            self._tail._next=None
        self._size-=1

    def deleteBeg(self):
        if self.isEmpty():
            print("The list is empty !")
            return
        if self._size==1:
            self._head=None
            self._tail=None
        else:
            self._head._next._prev=None
            self._head=self._head._next
        self._size-=1

    def delPos(self,pos):
        if self.isEmpty():
            print("The list is empty 1")
            return
        if pos >self._size or pos <1:
            print("Enter a valid position !")
            return
        if pos==1:
            self.deleteBeg()
            return
        if pos==self._size:
            self.deleteLast()
            return
        
        x=self._head
        count=1
        while(count<pos):
            x=x._next
            count+=1
        print(f"Deleted element: {x._ele}")
        x._prev._next=x._next
        if x._next:
            x._next._prev=x._prev
        self._size-=1

    def search(self,key):
        if self.isEmpty():
            print("the list is empty !")
            return -1
        x=self._head
        count=1
        while x:
            if key==x._ele:
                print("found ",key,"in position ",count)
                return
            else:
                x=x._next
                count+=1
        print("element not found")
        return -1


        




D=DoubleLL()
# Insert elements at the end
D.insertLast(1)
D.insertLast(2)
D.insertLast(3)

# Insert element at the beginning
D.insertBeg(0)
print("insert beg")
# Display the list
D.display()

# Insert element at a specific position
D.insertPos(4, 3)  # Insert 4 at position 3
print("insert pos 3")
D.display()

# Delete element from the beginning
D.deleteBeg()
print("del beg")
D.display()

# Delete element from the end
D.deleteLast()
print("del last")
D.display()

# Delete element from a specific position
D.delPos(2)  # Delete element at position 2
print("del pos 2")
D.display()

# Search for elements
D.search(3)  # Search for 3
D.search(10)  # Search for 10 (not present)


