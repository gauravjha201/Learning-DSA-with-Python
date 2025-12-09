class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LengthOfLoop:
    def __init__(self):
        self.head=None

    def Loop(self):
    #this is brute force approach
    #     my_dict=dict()  
    #     temp=self.head
    #     travel=0
    #     while temp is not None :
    #         if temp in my_dict :
    #             return travel-my_dict[temp.data]
    #         my_dict[temp.data]=travel
    #         travel+=1
    #         temp=temp.next
    #     return None

    #this optimal approach
        slow=self.head
        fast=self.head
        count=0
        while fast is not None and fast.next is not None :
            slow=slow.next
            fast=fast.next.next
            if slow == fast :
                slow=slow.next
                count=1
                while slow !=fast :
                    slow=slow.next
                    count+=1
                return count
        return 0



    
