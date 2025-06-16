class _Node:
    __slot__ = '_ele','_next'

    def __init__(self,ele,next):
        self._ele= ele
        self._next = next
class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    
    
    # def display(self):                  #o/p = 1 -> 2 -> 4 -> 5 ->
    #     x=self._head
    #     print("The linked list is : ")
    #     while x:
    #         print(x._ele,end=" ")
    #         x=x._next
    #         print("",end="-> ")
    #     print()
        
    def display(self):                     #o/p = 1 -> 2 -> 4 -> 5 
        x=self._head
        print("The linked list is : ",end="")
        while True:
            print(x._ele,end=" ")
            if x._next==None:
                break
            print("",end="-> ")
            x=x._next
        print()

    def search(self,e):
        x= self._head
        count = 0
        while x:
            if(e == x._ele):
                print("Element",e, "found in node : ",count+1)
                return 
            else:
                x=x._next
                count+=1
        print("Element", e,"not found in LL !")
        return -1
    
#----------inserting elements----------------------------------------------

    def addlast(self,e):
        new = _Node(e,None)
        if (self.isempty()):
            self._head=new
        else:
            self._tail._next=new
        self._tail=new
        self._size += 1

    def addbeg(self,e):
        # new = _Node(e,None)               #same implimnetation
        # if self.isempty():
        #     self._head = new
        #     self._tail = new
        # else:
        #     new._next=self._head
        #     self._head = new
        # self._size+=1

        new = _Node(e,self._head)           #efficient way
        self._head = new
        self._size+=1
        if self._tail:                      #if - (self._tail is None)
            self._tail = new

    def insertPos(self,pos,e):
        new = _Node(e,None)
        d = self._head
        count =1
        while (count < pos-1):
            d=d._next
            count+=1
        new._next=d._next
        d._next=new
        self._size+=1

#----------deleting elements----------------------------------------------

    def delLast(self):
        if self.isempty():                      #if the list is empty
            print("The list is empty !")
            return 
        
        if self._head._next is None:            #if the list has one node
            self._head = None
            self._tail = None
            print("Deleted the only node in the single LL !")
            self._size-=1
            return
        
        x = self._head                          #if the list has multiple nodes
        while x._next._next is not None:
            x=x._next
        print("Deleted the element node : ",x._next._ele)
        x._next=None
        self._tail= x
        self._size -=1

    def delPos(self, pos):
        if self.isempty():
            print("The list is empty !")
            return
        
        if pos < 1 or pos> self._size:
            print("Invalid postion entered !")
            return
        
        if pos ==1:
            print("Deleting the element : ",self._head._ele)
            self._head=self._head_next
            self._size-=1
            if self._head is None:
                self._tail=None
            return
        
        x=self._head
        count=1
        while count < pos -1:
            x=x._next
            count+=1
        
        print("Deleted node is ",x._next._ele)

        if (x._next == self._tail):
            self.tail=x
        
        x._next=x._next._next
        self._size-=1
            

        
            

#------------end of "Class Linked List"------------



L = LinkedList()

#adding at the end of the list
L.addlast(1)
L.addlast(2)
L.addlast(3)

#adding at the deginning of the list
L.addbeg(6)
L.addbeg(5)
L.addbeg(4)

#inserting at a position
#insertPos(pos,element)
L.insertPos(4,0)
L.insertPos(4,7)
L.insertPos(5,8)

#deleting at last of the list
L.delLast()

#deleting node at a certain position
L.delPos(5)
L.delPos(0)

#displaying the list
L.display()

#displaying the size of the list
print("Size of the Linked List is : ",len(L))

#searchin an element in the list
L.search(4)


