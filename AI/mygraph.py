class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdges(self, vertex1, vertex2, weight):
        self.addVertex(vertex1)
        self.addVertex(vertex2)

        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))

    def getVertices(self):
        return len(self.graph)

    def getEdges(self):
        return sum(len(edges) for edges in self.graph.values()) // 2

    def printGraph(self):
        for key in self.graph:
            print(key + ": ", self.graph[key])
            
graph = Graph()
with open("graph.txt", "r") as f:
    for line in f:
        vertex1, vertex2, weight = line.strip().split(',')
        weight = int(weight)
        graph.addEdges(vertex1.strip(), vertex2.strip(), weight)

print("Number of vertices:", graph.getVertices())
print("Number of edges:", graph.getEdges())

graph.printGraph()