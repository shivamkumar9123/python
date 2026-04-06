class Queue:
    def __init__(self):
        self.item=[]

    def isEmpty(self):
        return len(self.item)==0
            
    def insertAtEnd(self,value):
        self.item.append(value)
    def deleteAtFront(self):
        if(self.isEmpty()):
            print("Dequeue is empty") 
        else:
            return self.item.pop(0)
        
    def insertAtFront(self,value):
        self.item.insert(0,value)

    def deleteAtEnd(self):
        if(self.isEmpty()):
            print("Dequeue is empty")
        else:
           return self.item.pop()

Dq=Queue()
Dq.insertAtEnd(10)
Dq.insertAtFront(20)
Dq.insertAtEnd(30)
Dq.insertAtEnd(40)
Dq.insertAtFront(50)
print(Dq.deleteAtEnd())
print(Dq.deleteAtEnd())
print(Dq.deleteAtFront())
print(Dq.deleteAtFront())
print(Dq.deleteAtEnd())
Dq.deleteAtEnd()
Dq.deleteAtFront()