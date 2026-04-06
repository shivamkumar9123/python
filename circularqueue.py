class circularqueue:
    def __init__(self,size):
        self.size=size
        self.item=[None]*size
        self.front=self.rear=-1

    def enqueue(self,value):
        if((self.rear + 1) % self.size == self.front):
            print("queue is full ")
        elif self.front==-1:
            self.front=self.rear=0
            self.item[self.rear]=value
        else:
            self.rear=(self.rear + 1)%self.size
            self.item[self.rear]=value
    def dequeue(self):
        if(self.front==-1):
            print("queue is empty")
        elif self.front==self.rear:
            print(self.item[self.front])
            self.rear=self.front=-1
        else:
            print(self.item[self.front])
            self.front =(self.front + 1) % self.size


c=circularqueue(4)
c.enqueue(10)
c.enqueue(20)
c.enqueue(30)
c.enqueue(40)
c.enqueue(50)
c.dequeue()
c.enqueue(60)
c.enqueue(70)
c.enqueue(80)
c.dequeue()
c.dequeue()
c.dequeue()
c.dequeue()
c.dequeue()





