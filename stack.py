class Stack():
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.lst=[None]*self.maxsize
        self.top=-1
        
    def push(self,data):
        if(self.top==self.maxsize-1):
            print("stack is full")
        else:
            self.top+=1
            self.lst[self.top]=data
            
    def pop(self):
        if(self.top==-1):
            print("stack  is empty")
        else:
            self.top-=1
    
    def display(self):
        if(self.top==-1):
            print("stack has no elements")
        else:
            index=self.top
            if (index>=0):
                print(self.lst[self.top])
                 
            
s=Stack(3)
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.push(100)
s.display()
            
        
