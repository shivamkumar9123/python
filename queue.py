class node:
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return len(self.item)==0
    def insert(self,value):
        self.item.append(value)

    def delete(self):
        if(self.isEmpty()):
            print("Queue is empty")
        else:
            return self.item.pop(0)
        
q=node()
q.insert(10)
q.insert(20)
q.insert(30)
print(q.delete())
print(q.delete())
print(q.delete())
q.delete()


