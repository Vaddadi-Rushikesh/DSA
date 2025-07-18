class StackArray:
    __slot__='data'
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)
    def isEmpty(self):
        return len(self.data)==0
    
    def push(self,a):
        self.data.append(a)
        return
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.data.pop()
    
    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.data[-1]
    
s=StackArray()
s.push(1)
s.push(2)
s.push(3)

print(s.__len__())
print("data",s.data)
print("popped",s.pop())
print("popped",s.pop())
print("data",s.data)