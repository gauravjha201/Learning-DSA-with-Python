class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class StackusingDLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self,item):
        newnode=Node(item)
        if self.head is None:
            self.tail=self.head=newnode
        self.tail.next=newnode
        newnode.prev=self.tail
        self.tail=newnode

    def pop(self):
        if self.head is None :
            print("Empty Stack")
        if self.head.next is None :
            del self.head
            return 
        self.tail=self.tail.prev
        
        

        
