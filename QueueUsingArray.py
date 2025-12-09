class Queue:
    def __init__(self):
        self.item=[]
    def enqueue(self,x):
        self.item.append(x)
    def isempty(self):
        return len(self.item)==0
    def dequeue(self):
        if len(self.item)==0:
            print("queue is empty")
            return
        x=self.item.pop(0)
        return x
    def size(self):
        x= len(self.item)
        return x
    def front(self):
        if self.isempty():
            print("queue is empty")
            return
        return self.item[0]
    def rear(self):
        if self.isempty():
            print("queue is empty")
            return 
        return self.item[-1]
    
queue