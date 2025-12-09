from collections import deque
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def BFS(self,root):
    result=[]
    queue=deque([])
    queue.append(root)
    while len(queue)!=0:
        e=queue.popleft()
        result.append(e.data)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    return result
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.right=node(7)

print(BFS(root))