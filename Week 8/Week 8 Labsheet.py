'''implemented dijkstra's algorithm to previous graph structure '''
class Graph(object):
    def __init__(self):
        self.nodes = []
    def addNode(self,value):
        self.nodes.append(value)
    def addEdge(self,node1,node2,weight):
        for i in range(len(self.nodes)):
            if self.nodes[i] == node1:
                self.nodes[i].addEdge([node2,weight])
            if self.nodes[i] == node2:
                self.nodes[i].addEdge([node1,weight])
                
    '''implemented dijkstra's procedure'''            
    def dijkstra(self,start,finish):
        currentNode = start #makes curent node the start node
        queue = [start] #adds the start node to the queue
        path = []
        for i in range(len(self.nodes)):    #loop to make every nodes total weight infinate
            self.nodes[i].totalWeight = float("inf") 
        start.totalWeight = 0   #makes the start nodes totalweight 0
        visited = []            #creates an empty list for visited
        while currentNode != finish: #loops until it reaches the finish node
            currentNode = queue.pop(0)  #front of the queue becomes the current node
            for i in range(len(currentNode.edges)): #loop goes through all of current nodes edges
                adjNode = currentNode.edges[i]      #adjacent node becomes next connected node
                if (currentNode.totalWeight + adjNode[1]) < adjNode[0].totalWeight:
                    adjNode[0].totalWeight = currentNode.totalWeight + adjNode[1]   #calculates new total weight
                    adjNode[0].pre = currentNode #record the path
                    queue.append(adjNode[0]) #adds the adjacent node to the priority queue
                    queue.sort(key = lambda x:currentNode.totalWeight) #re-sorts the priority queue by total weights of nodes  
            visited.append(currentNode) #add the current node to the list of visited nodes
        while currentNode != start:
            path.append(currentNode.label)
            currentNode = currentNode.pre
        path.append(start.label)
        path.reverse()
        return(path)
        
class Vertex(object):
    def __init__(self,value):
        self.label = value
        self.edges = []
        self.totalWeight = None
        self.pre = None
    def addEdge(self,node):
        self.edges.append(node)
    def __str__(self):
        return ("Vertex{0}".format(self.label))
    

if __name__ == '__main__':
    
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

    g.addEdge(v1,v2,5)
    g.addEdge(v1,v3,2)
    g.addEdge(v2,v4,7)
    g.addEdge(v3,v4,4)
    g.addEdge(v3,v5,8)
    g.addEdge(v4,v5,3)

    print(g.dijkstra(v1,v5))

