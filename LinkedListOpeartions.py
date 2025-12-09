class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singly_linked_list:
    def __init__(self):
        self.head=None
    def append(self,data):
        newnode=node(data)
        if self.head is  None:
            self.head=newnode
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newnode
    def tarversal(self):
        if self.head is None:
            return None
        
        else:
            curr=self.head
            while curr.next is not None:
                print(curr.data,end=" ")
                curr=curr.next

    def insert_at_index(self,index,data):
        newnode=node(data)
        if self.head is None:
            print("LL is Empty")
            return
        elif index==0:
            newnode.next=self.head
            self.head=newnode
        else:
            curr=self.head
            count=0
            while curr is not None and count<index-1:
                curr=curr.next
                count+=1
                if curr is None:
                    print("index out of range")
                    return 
                newnode.next=curr.next
                curr.next=newnode
            
    def delete_at_index(self,index):
        if self.head is None:
            print("LL is empty")
            return
        elif index==0:
            self.head=self.head.next
        else:
            curr=self.head
            count=0
            while curr is not None and count<index-1:
                curr=curr.next
                count+=1
            if curr is None or curr.next is None:
                print("Index is out of range")
                return
            curr.next=curr.next.next


sll=singly_linked_list()          
sll.append(0)
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.insert_at_index(2,5)
sll.delete_at_index(3)
sll.tarversal()
         



        