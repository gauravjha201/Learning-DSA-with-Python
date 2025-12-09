class node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=start
    
    def is_empty(self):
        return self.start==None
    

    def insert_at_start(self,data):
        n=node(data,self.start)
        self.start=n


    def insert_at_last(self,data):
        n=node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None :
                temp=temp.next
                temp.next=n
        else:
            self.start=n


    def search(self,data):
        if self.is_empty():
            print("Linkedlist is empty")
        else:
            temp=self.start
            while temp is not None:
                if(temp.item==data):
                    return temp
                temp=temp.next
                return None
            

    def insert_after(self,data,temp):
        while temp is not None:
            n=node(data,temp.next)
            temp.next=n
            

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next

myList=SLL()#driver code
myList.insert_at_start(20)
myList.insert_at_start(10)
# myList.insert_at_last(30)
myList.insert_after(myList.search(20),25)
myList.print_list()
print()

