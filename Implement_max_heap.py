class solution:
    def __init__(self):
        self.arr=[]
        self.count=0
    def heapify_up(self,arr,ind):
        parent_ind=(ind-1)/2
        if parent_ind>0 and arr[ind]>arr[parent_ind]:
            arr[ind],arr[parent_ind]=arr[parent_ind],arr[ind]
            self.heapify_up(arr,parent_ind)
    
    def heapify_down(self,arr,ind):
        n=len(arr)
        large_ind=ind
        left_ind=2*ind+1
        right_ind=2*ind+2
        if left_ind<n and arr[left_ind]>arr[large_ind]:
            large_ind=left_ind
        if right_ind<n and arr[right_ind]>arr[large_ind]:
            large_ind=right_ind
        if large_ind!=ind:
            arr[ind],arr[large_ind]=arr[large_ind],arr[ind]
            self.heapify_down(arr,large_ind)

    def initializeheap(self):
        self.arr.clear()
        self.arr.count=0

    def insert(self,key):
        self.arr.append(key)
        self.heapify_up(self.arr,self.count)
        self.count+=1
    
    def getMax(self):
        return self.arr[0] if self.count>0 else None
    def isEmpty(self):
        return self.count==0
    def size(self):
        return self.count

    def extractMax(self):
        if self.count<1:
            return None
        ele=self.arr[0]
        self.arr[0],self.arr[self.count-1]=self.arr[self.count-1],self.arr[0]
        self.arr.pop()
        self.count-=1
        if self.count>0:
            self.heapify_down(self.arr,0)
        return ele

    def chanegekey(self,index,new_val):
        if self.arr[index]>new_val:
            self.arr[index]=new_val
            self.heapify_down(self.arr,index)
        else:
            self.arr[index]=new_val
            self.heapify_up(self.arr,index)
            