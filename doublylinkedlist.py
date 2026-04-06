class node:
    def __init__(self,value=None):
         self.data=value
         self.next=None
         self.prev=None
class doublyLinkedList:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,value):
        temp=node(value)
        if(self.head==None):
            self.head=temp
            return
        t=self.head
        while(t.next !=None):
            t=t.next
        t.next=temp
        temp.prev=t
    
    def insertAtBeg(self,value):
        temp=node(value)
        if(self.head==None):
            self.head=temp
            return
        else:
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
    def insertAtMid(self,value,x):
        if(self.head==None):
            print("List is empty")
            return
        t=self.head
        while(t.next !=None):
            if(t.data ==x):
                 break
            else:
                t=t.next

        if(t.data==None):
            print("value not found")
            return
        temp=node(value)
        temp.next=t.next
        t.next.prev=temp
        temp.prev=t

    def printLL(self):
        t1=self.head
        while (t1 !=None):
            print(t1.data,end="<->")
            t1=t1.next
    
    def deletedElement(self,value):
        if(self.head==None):
            print("linkedlist is empty:")
            return
        t=self.head
        if(t.data==value):
            self.head=t.next
            self.head.prev=None
            return
        while(t.next !=None):
            if(t.data==value):
               t.prev.next=t.next
               t.next.prev=t.prev
               return
            else:
                t=t.next
        if(t.data ==value):
            t.prev.next=None


obj= doublyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtEnd(50)
obj.insertAtBeg(5)
obj.insertAtMid(60,40)
obj.deletedElement(5)
obj.deletedElement(30)
obj.printLL()
