class node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
    def insert(root,value):
        if(root ==None):
            return node(value)
        if(root.data==value):
            return root
        if(root.data>value):
            root.left=node.insert(root.left,value)
        else:
            root.right=node.insert(root.right,value)
        return root
def get_successor(root):
    root= root.right
    while(root !=None and root.left !=None):
        root=root.left
    return root
           
def deleted(root,value):
    if(root ==None):
        return root
    if(root.data >value):
        root.left=deleted(root.left,value)
    elif(root.data<value):
          root.right=deleted(root.right,value)
    else:
        if(root.right==None):
            return root.left
        if(root.left==None):
            return root.right
        else:
            succ=get_successor(root)
            root.data=succ.data
            root.right=deleted(root.right,succ.data)
            return root
def InOrder(root):
    if(root !=None):
        InOrder(root.left)
        print(root.data,end=" ")
        InOrder(root.right)

root =node.insert(None,20)
root=node.insert(root,15)
root=node.insert(root,30)
root=node.insert(root,25)
root=node.insert(root,23)
root=node.insert(root,40)
root=node.insert(root,50)

InOrder(root)
deleted( root,23)
print("\n")
