class node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

def preorder(root):
    if(root !=None):
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
          
       
        
root=node(1)
root.left=node(3)
root.right=node(5)
root.left.left=node(2)
root.left.right=node(4)
root.right.right=node(8)
preorder(root)

