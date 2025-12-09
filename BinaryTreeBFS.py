from collections import deque
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
def levelorder(node):
    result=[]
    queue=deque([])
    queue.append(node)
    while queue:
        e=queue.popleft()
        result.append(e.data)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    return result
print(levelorder(one))

        