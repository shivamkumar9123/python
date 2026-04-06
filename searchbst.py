class node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
    def search(root,value):
        if(root==None):
            print("element not found:", end="\n")
            return
        if(root.data ==value):
            print("element found:" ,end="\n")
            return
        if(root.data>value):
             node.search(root.left,value)
        else:
            node.search(root.right,value)

def Inorder(root):
    if(root !=None):
        Inorder(root.left)
        print(root.data, end=" ")
        Inorder(root.right)
root=node(20)
root.left=node(15)
root.right=node(30)
root.right.left=node(25)
root.right.left.left=node(23)
root.right.right=node(40)
root.right.right.right=node(50)
Inorder(root)
node.search(root,23)
node.search(root,100)