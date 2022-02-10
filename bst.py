#MIDN ESHLEMAN
#221938

import sys

#STEP ONE
class ArraySet:

    def __init__(self):
        self.array = []

    def insert(self,key):
        self.array.append(key)
#returns true if the specified key is in the array
#returns false if not
    def __contains__(self,key):
        if key in self.array:
            return True
        else:
            return False

#STEP TWO
#create a node class
class Node:
    def __init__(self,val=None):
        self.val = val
        self.right = None
        self.left = None

    def __str__(self):
        return (str(self.val))

class TreeSet:
    def __init__(self):
        self._root = None


    def insert(self,key=None):
        refNode = Node(key)
        if self._root:
            self.__insert(self._root, refNode)
        else:
            self._root = refNode

    def __insert(self, currentNode, refNode):
        if(refNode.val > currentNode.val):
            if (currentNode.right == None):
                currentNode.right = refNode
            else:
                self.__insert(currentNode.right, refNode)
        else:
            if (currentNode.left == None):
                currentNode.left = refNode
            else:
                self.__insert(currentNode.left, refNode)          

    def __contains__(self,key):
        if (self.keycheck(key,self._root)):
            return True
        else:
            return False
    
    def keycheck(self, key, node):
        if not Node:
            return None
        elif node.val == key:
            return Node
        elif key < node.val:
            return self.keycheck(key,node.right)
    
    def printTree(_root):
        if self._root:
            printInorder(_root.left)
            print(root.val)
            printInorder(_root.right)

if __name__ == '__main__':
    main()