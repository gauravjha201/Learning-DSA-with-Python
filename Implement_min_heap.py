class solution:
    def __init__(self):
        self.arr=[]
        self.count=0
    def heapify_up(self,arr,ind):
        parent_ind=(ind-1)//2
        if ind>0 and arr[ind]<arr[parent_ind]:
            arr[ind],arr[parent_ind]=arr[parent_ind],arr[ind]
            self.heapify_up(arr,parent_ind)
    
    def heapify_down(self,arr,ind):
        n=len(arr)
        small_ind=ind
        left_ind=ind*2+1
        right_ind=ind*2+2
        if left_ind<n and arr[left_ind]<arr[small_ind]:
            small_ind=left_ind
            self.heapify_down(arr,small_ind)
        if right_ind<n and arr[right_ind]<arr[small_ind]:
            small_ind=right_ind
            self.heapify_down(arr,small_ind)
        if small_ind!=ind:
            arr[small_ind],arr[ind]=arr[ind],arr[small_ind]
            self.heapify_down(arr,small_ind)
    
    def initializeHeap(self):
        self.arr.clear()
        self.count=0
    
    def insert(self,key):
        self.arr.append(key)
        self.heapify_up(self.arr,self.count)
        self.couunt+=1
    
    def changekey(self,index,new_val):
        if self.arr[index]>new_val:
            self.arr[index]=new_val
            self.heapify_up(self.arr,index)
        else:
            self.arr[index]=new_val
            self.heapify_down(self.arr,index)

    def extractMin(self):
        if self.count==0:
            return None
        ele=self.arr[0]
        self.arr[0],self.arr[self.count-1]=self.arr[self.count-1],self.arr[0]
        self.arr.pop()
        self.count-=1
        if self.count>0:
            self.heapify_down(self.arr,0)
        return ele
    
    def isEmpty(self):
        return self.count==0

    def size(self):
        return self.count
    def getMin(self):
        return self.arr[0] if self.count>0 else None
    
def main():
    heap=solution()
    heap.initializeHeap()

    heap.insert(4)
    heap.insert(5)
    heap.insert(10)
    heap.insert(2)

    print(f'MIN :{heap.getMin()}')
    print(f'Is empty :{heap.isEmpty()}')
    print(f'heap_size :{heap.size()}')

    print("Extracting Min")
    heap.extractMin()

    print("changing index 0 to 10")
    heap.changekey(0,10)

        
