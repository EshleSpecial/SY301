class Node:
  def __init__(self, data):
    self.data = data
    self.nextNode = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add2Front(self, data):
    '''Same as it has always been.'''
    newNode = Node(data)
    if self.tail == None:
        self.tail = newNode
    else:
        newNode.nextNode = self.head

  def printInOrder(self):
    '''Prints each element of the linked list, one on each line'''
    pass
  def __printInOrder(self, node):
    '''helper method for printInOrder'''
    pass

  #These functions will also need helper methods like printInOrder, you will have to create them
  def isIn(self, element):
    '''Returns True or False, indicating if element is in the list'''
    pass

  def isInTimes(self, element):
    '''Returns an integer, which is the number of times element appears in 
    the list'''
    pass

  def get(self, i):
    '''Returns the data at index i (counting from 0).  You may assume i is a
    valid index'''
    pass

  def addBefore(self, findElement, addElement):
    '''Adds addElement to the list, so that it appears right before the first
    appearance of findElement in the list.  If findElement is not in the list,
    addElement should be added to the end of the list.'''
    pass