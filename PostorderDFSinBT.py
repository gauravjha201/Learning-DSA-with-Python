class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def Postorder_traversal(node):
    if node==None:
        return
    Postorder_traversal(node.left)
    Postorder_traversal(node.right)
    print(node.data,end=" ")

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

print(Postorder_traversal(root))
        