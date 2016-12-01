'''Program implementing a graph using an adjaceny list in object orientated'''

class Graph(object):            #creates a graph object
    def __init__(self): #runs when object is assigned to new value
        self.nodes = []         #creates a nodes atribute using a list 
    def addNode(self,value):
        self.nodes.append(value) #adds value to list of nodes
    def addEdge(self,node1,node2):
        for i in range(len(self.nodes)): 
            if self.nodes[i] == node1:   #check if node1 is in graph
                self.nodes[i].addEdge(node2) #adds node2 to current nodes edges
            if self.nodes[i] == node2:   #check if node2 is in graph
                self.nodes[i].addEdge(node1) #adds node1 to current nodes edges
                
class Vertex(object):           #creates a vertex object
    def __init__(self,value):   #runs when object is assigned to new value
        self.label = value      #creates a label attribute and sets it to value
        self.edges = []         #creates a edges atribute using a list
    def addEdge(self,node):
        self.edges.append(node) #adds node to the list of edges


if __name__ == '__main__':
#'''creates the graph and nodes then enters all nodes and edges
#to graph and prints adjacency list'''
    g = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)
    g.addNode(v1)
    g.addNode(v2)
    g.addNode(v3)
    g.addNode(v4)
    g.addNode(v5)
    
    g.addEdge(v1,v2)
    g.addEdge(v2,v4)
    g.addEdge(v3,v4)
    g.addEdge(v3,v5)
    g.addEdge(v4,v5)

for i in range(len(g.nodes)):
    print("Node {0} has the following edges:".format(g.nodes[i].label))
    for j in range(len(g.nodes[i].edges)):
        print(g.nodes[i].edges[j].label)
        
