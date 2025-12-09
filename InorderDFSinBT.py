class Node :
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def Inorder_traversal(node):
    if node==None :
        return 
    Inorder_traversal(node.left)
    print(node.data,end=" ")
    Inorder_traversal(node.right)


root=Node(1) 
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.right=Node(5)

print(Inorder_traversal(root))
        