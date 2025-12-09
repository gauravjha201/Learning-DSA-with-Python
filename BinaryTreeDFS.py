class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

one=Node("1")
two=Node("2")
three=Node("3")
four=Node("4")
five=Node("5")
six=Node("6")
seven=Node("7")
eight=Node("8")
nine=Node("9")

one.left=two
one.right=three
two.left=four
two.right=five
three.left=six
three.right=seven
four.left=eight
four.right=nine

def preorder(node):#root left right
    if node==None:
        return 
    print(node.data,end=" ")
    preorder(node.left)
    preorder(node.right)
# preorder(one)
def inorder(node):#left root right
    if node==None:
        return 
    inorder(node.left)
    print(node.data,end=" ")
    inorder(node.right)
# inorder(one)
def postorder(node):#left right root
    if node==None:
        return 
    postorder(node.left)
    postorder(node.right)
    print(node.data)
postorder(one)

