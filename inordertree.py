class node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

def InOrder(root):
    if(root !=None):
        InOrder(root.left)
        print(root.data,end=" ")
        InOrder(root.right)

root=node(1)
root.left=node(3)
root.right=node(5)
root.left.left=node(2)
root.left.right=node(4)
root.right.right=node(8)
InOrder(root)


        