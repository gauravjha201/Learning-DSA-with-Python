class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
drinks=Node("drinks")
hot=Node("hot")
cold=Node("cold")
coffee=Node("coffee")
tea=Node("tea")
cola=Node("cola")
fanta=Node("fanta")

drinks.left=hot
drinks.right=cold

hot.left=coffee
hot.right=tea

cold.left=cola
cold.right=fanta

print(drinks.right.left.data)
