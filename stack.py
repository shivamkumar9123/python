class stack:
    def __init__(self):
        self.list=[]
    def length(self):
        return len(self.list)
    def push(self,value):
        self.list.insert(0, value)
    def peek(self):
        if len(self.list)==0:
            raise Exception("stack is empty")
        else:
            return self.list[0]
    def pop(self):
        if len(self.list)==0:
            raise Exception("stack is empty")
        else:
            return self.list.pop(0)
stk=stack() 
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
print(stk.peek())
print(stk.pop())
print("stack elements:",stk.list)