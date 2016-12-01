'''Graph with implemented DFS and BFS functions and writes results to text file'''
class Graph(object):
    def __init__(self):
        self.nodes = []
    def addNode(self,value):
        self.nodes.append(value)
    def addEdge(self,node1,node2):
        for i in range(len(self.nodes)):
            if self.nodes[i] == node1:
                self.nodes[i].addEdge(node2)
            if self.nodes[i] == node2:
                self.nodes[i].addEdge(node1)
    '''implemented BFS'''
    def BFS(self,startNode):
        Queue = [] #creates list for queue
        visited = [] #creates list for visited nodes
        Queue.append(startNode) #adds starting node to the queue
        while Queue != []: #loops until queue is empty
            currentNode =  Queue.pop(0) #makes current node the first value in the queue
            if currentNode.label not in visited: #checks if current node already in visited
                visited.append(currentNode.label) #adds the current node to visited
                for i in range(len(currentNode.edges)): #loop to add every edge connected to current node to the queue
                    Queue.append(currentNode.edges[i])
        return (visited) #return the list of visited nodes
    '''implemented DFS'''        
    def DFS(self,startNode):
        stack = [] #creates list for stack
        visited = [] #creates list for visited nodes
        stack.append(startNode) #adds starting node to the stack
        while stack != []: #loops until queue is empty
            currentNode = stack.pop() #pops top value from the stack to current node
            if currentNode.label not in visited:
                visited.append(currentNode.label)   #adds the node to visited if it hasnt already
                for i in range(len(currentNode.edges)):
                    stack.append(currentNode.edges[i])  #loop to add every edge connected to the current node onto the stack
        return(visited) #return the list of visited nodes
    
class Vertex(object):
    def __init__(self,value):
        self.label = value
        self.edges = []
    def addEdge(self,node):
        self.edges.append(node)        

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

    g.addEdge(v1,v2)
    g.addEdge(v2,v4)
    g.addEdge(v3,v4)
    g.addEdge(v3,v5)
    g.addEdge(v4,v5)

    print("Breadth first search result: %s" % g.BFS(v1))
    print("Depth first search result: %s" % g.DFS(v1))
    
'''implementation to adding the results to a text file'''
    text_file = open("Results.txt","w")     #opens the text file ready to overwrite
    text_file.write("Breadth first search result: %s \n" % g.BFS(v1)) #writes the results to the file
    text_file.write("Depth first search result: %s" % g.DFS(v1))
    text_file.close() #saves and closes the file
