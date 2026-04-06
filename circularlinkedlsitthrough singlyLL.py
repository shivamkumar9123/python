class node:
    def __init__(self,info):
        self.next=None
        self.data=info
class circularlinkedlist:
    def __init__(self):
        self.head=None

    def insertAtEnd(self,value):
        temp=node(value)
        if(self.head==None):
           self.head=temp
           temp.next=temp
           return
        t1=self.head
        while(t1.next!=self.head):
            t1=t1.next
            t1.next=temp
        else:
         temp.next=self.head
    def printLL(self):
        if(self.head==None):
            print("list is empty")
            return
        t1=self.head
        while (t1.next !=self.head):
            print(t1.data,end="->")
            t1=t1.next
            if(t1==self.head):
                break
            print("(back to head)")
obj=circularlinkedlist()
obj.insertAtEnd(10) 
obj.insertAtEnd(20) 
obj.insertAtEnd(30) 
obj.insertAtEnd(40) 
obj.insertAtEnd(50) 
obj.insertAtEnd(60) 
obj.printLL()          