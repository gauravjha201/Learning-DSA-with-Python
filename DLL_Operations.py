class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doubly_Linked_List:
    def __init__(self):
        self.head=None
    
    def insert_at_head(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode

    def append(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next is None :
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp
    
    def insert_in_between(self,data,index):
        newnode=Node(data)
        if index==0 :
            self.insert_at_head(data)
            return 
        temp=self.head
        count=0
        while temp and count<index-1:
            temp=temp.next
            count+=1
        
        if temp is None :
            print("index is out of Bound")
            return
        newnode.next=temp.next
        newnode.prev=temp
        if temp.next:
            temp.next.prev=newnode
            temp.next=newnode

    def traverse(self):
        temp=self.head
        while temp.next is not None:
            print(temp.data)
            temp=temp.next

    def delete_head(self):
        if self.head is None:
            return None
        
        temp=self.head
        self.head=temp.next
        if self.head:
            self.head.prev=None
        del temp
    
    def delete_last(self):
        if self.head is None:
            return None
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        if temp.prev:
            temp.prev.next=None
        del temp

    def delete_in_middle(self,key):
        if self.head is None :
            return None
        temp=self.head

        if temp.data==key:
            self.head=temp.next
            temp.next.prev=None
        else:
            self.head=None
        return

        while temp and temp.next is not None :
            temp=temp.next
            if temp.data==key:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
                del temp
                return
           
        print("Node is not found")




    
    def delete_in_between(self,index):
        if self.head is None :
            return None
        
        if index ==0:
            self.delete_head()
            return
        
        temp=self.head
        count=0
        while temp and count <index-1:
            count+=1
            temp=temp.next
        
        if temp is None or temp.next is None :
            print("Index out of bound")
            return
        if temp.next.next is None :
            self.delete_last()
            return 
        
        temp.next=temp.next.next
        temp.next.prev=temp


    def Reverse_DLL(self):# this is Brute force approach
        stack=[]
        temp=self.head
        while temp is not None :
            stack.append(temp.data)
            temp=temp.next
        temp=self.head
        while temp is not None :
            e=stack.pop()
            temp.data=e
            temp=temp.next
        return self.head
    
    def Reverse_DLL_Optimal(self):
        temp=self.head
        prev=None
        while temp is not None :
            front=temp.next

            temp.next=prev
            temp.prev=front

            prev=temp
            temp=front

        return prev

    def DeleteAllOccurrenceOfkey(self,key):
        if self.head.next is None and self.head.data is key :
            return None 
        
        temp=self.head
        prev=None
        newnode=self.head
        while temp is not None :
            if temp.data==key :
                if temp.prev is not None :
                    prev.next=temp.next
                    if temp.next is not None :
                        temp.next.prev=prev
                    if temp == newnode :
                        newnode=newnode.next

            prev=temp
            temp=temp.next
        
        return newnode
    

    def PairOfSumInSortedDLL(self,key):#this is brute force approach
        result=[]
        temp1=self.head
        while temp1 is not None :
            temp2=temp1.next
            while temp2 is not None :
                if temp1.data +temp2.data==key :
                    result.append([temp1.data,temp2.data])
                temp2=temp2.next
            temp1=temp1.next
        return result
    
    def PairOfSumInSortedDLLBetter(self,key):
        myset=set()
        result=[]
        temp=self.head
        while temp is not None :
            remain=key-temp.data
            if remain in myset :
                result.append([remain,temp.data])
            myset.add(temp.data)
            temp=temp.next
        return result 
    
    def PairOfSumInSortedDLLOptimal(self,key):
        result=[]
        left=self.head
        right=self.head
        while right.next is not None :
            right =right.next
        while left.next is not None and right.next is not None and left.data < right.data :
            if left.data + right.data ==key :
                result.append([left.data,right.data])
                left=left.next
                right=right.prev
            elif left.data+right.data>key :
                right=right.prev
            else:
                left=left.next
            
        return result
    
    def RemoveDuplicatesInSortedDLL(self):
        curr=self.head
        while curr.next is not None :

            if curr.data == curr.prev.data :
                if curr.prev is self.head :
                    curr.prev=None
                    self.head=curr
                curr.prev.prev.next=curr
                curr.prev=curr.prev.prev

            curr=curr.next



    

