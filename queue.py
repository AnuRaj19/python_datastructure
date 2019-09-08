class Queue():
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.lst=[None]*self.maxsize
        self.front=0
        self.rear=-1
    def enqueue(self,data):
        if(self.rear==self.maxsize-1):
            print("queue is full")
        else:
            self.rear+=1
            self.lst[self.rear]=data
    def dequeue(self):
        if(self.rear==-1):
            print("queue has no elements")
        else:
            self.front+=1
    def display(self):
        print(self.lst[self.front])



q=Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.dequeue()
q.display()
