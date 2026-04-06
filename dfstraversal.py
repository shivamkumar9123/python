class dfs:
    def __init__(self,vertex):
        self.mat=[[0]*vertex for x in range(vertex)]
        self.size=vertex
    
    def add_Edge(self,src,dest):
        if(0<=src<self.size and 0<=dest<self.size):
            self.mat[src][dest]=1
            self.mat[dest][src]=1
        else:
            print("invalid edges")
    def print(self):
        for row in self.mat:
            print(" ".join (map(str,row)))

    def dfs(self,src):
        visited=[False]*self.size
        stack=[src]
        while(stack):
            v =stack.pop()
            if(visited[v]==False):
                print(v,end="->")
                visited[v]=True

            for i in range(self.size):
                if self.mat[v][i]==1 and visited[i]==False:
                    stack.append(i)
                


g=dfs(6)
g.add_Edge(0,1)
g.add_Edge(0,2)
g.add_Edge(2,3)
g.add_Edge(2,4)
g.add_Edge(3,5)
g.add_Edge(4,5)
g.dfs(0)





