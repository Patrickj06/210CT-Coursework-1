class Node(object):
    def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None

class List(object):
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,n,x):
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
        if x.next!=None:
            x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x
    '''implemented delete node function to code provided '''        
    def delete(self,n):
        if n.prev != None: #check if node is at the start of list
            n.prev.next = n.next #make previous node point to the next node from current node
        else:
            l.head = n.next #make next node the head of list 
        if n.next != None: #check if node is at the end of list 
            n.next.prev = n.prev #make next node's previous to point to current node's previous
        else:
            l.tail = n.prev #make the previous node the tail of the list
            
    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print ("List: ",",".join(values))
                  
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.delete(l.head)
    l.display()
