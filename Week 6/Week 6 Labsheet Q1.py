#include <iostream>

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None


        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
  
'''implemented in order function to the tree sort algorithm iteratively '''
def in_order(tree):
    '''if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)'''
    done = False
    stack = []
    while (not done):       #loops until done is true
        if tree != None:        #checks current node is not empty
            stack.append(tree)  #adds current node to the stack
            tree = tree.left    #moves down the left branch
        elif len(stack) != 0:   #checks stack is not empty
            tree = stack.pop()  #makes the top of stack the current node
            print(tree.value)   #outputs the value of current node
            tree = tree.right   #moves down the right branch
        else:
            done = True         #ends loop
def tree_sort(aList):
    t=tree_insert(None,aList[0]);
    for i in range(1,len(aList)):
        tree_insert(t,aList[i])
    in_order(t)

if __name__ == '__main__':
    
  tree_sort([6,10,5,2,3,4])
