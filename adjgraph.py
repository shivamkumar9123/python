class graph:
    def __init__(self):
        self.adjList={}
    def add_vertex(self,vertex):
        if vertex not in self.adjList:
            self.adjList[vertex]=[]

    def add_edges(self,src,dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adjList[src].append(dest)
        self.adjList[dest].append(src)

    def printgraph(self):
       for vertex in self.adjList:
           print(vertex,"->",self.adjList[vertex])
g=graph()
g.add_edges(1,2)
g.add_edges(1,4)
g.add_edges(2,4)
g.add_edges(2,3)
g.add_edges(3,4)
g.add_edges(4,5)
g.add_edges(3,5)
g.printgraph()

       

