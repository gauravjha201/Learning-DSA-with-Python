class Node :
    def __init__(self,data):
        self.data=data
        self.next=None

class singly_linkedlist :
    def __init__(self):
        self.head=None
    def append(self,data):
        newnode=Node(data)
        if self.head is None :
            self.head=newnode
        else:
            curr=self.head
            while curr.next is not None :
                curr=curr.next
            curr.next=newnode
    
    def traversal(self):
        if self.head is None :
            print("SLL is empty")
        else:
            curr=self.head
            while curr is not None :
                print(curr.data,end=" ")
                curr=curr.next
            print()

sll=singly_linkedlist()
sll.append(10)
sll.append(20)
sll.append(30)
sll.traversal()