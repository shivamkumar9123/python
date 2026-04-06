class node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
def PostOrder(root):
    if(root !=None):
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data,end=" ")
 
root=node(1)
root.left=node(3)
root.right=node(5)
root.left.left=node(2)
root.left.right=node(4)
root.right.right=node(8)
PostOrder(root)