import math

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
    if (self.head == None):
      self.head = newNode
      self.tail = newNode
    else:
      tempNode = self.head
      self.head = newNode
      newNode.nextNode = tempNode
    return 0

  def printInOrder(self):
    '''Prints each element of the linked list, one on each line'''
    self.__printInOrder(self.head)
    return 0

  def __printInOrder(self, node):
    '''helper method for printInOrder'''
    if node == self.tail:
      print(str(node.data) + " ")
      return
    else:
      print(str(node.data) + " ")
      nextNode = node.nextNode
      self.__printInOrder(nextNode)

  #These functions will also need helper methods like printInOrder, you will have to create them
  def isIn(self, element):
    '''Returns True or False, indicating if element is in the list'''
    return self.__isIn(element, self.head)

  def __isIn(self,element,node):
    if node.data == element:
      return True
    if node.nextNode == None:
      return False
    return self.__isIn(element, node.nextNode)

  def isInTimes(self, element):
    '''Returns an integer, which is the number of times element appears in 
    the list'''
    counter = self.__isInTimes(element, self.head, 0)
    return counter

  def __isInTimes(self,element,node,count):
    if node.data == element:
      count += 1
    if node.nextNode == None:
      return count
    return self.__isInTimes(element, node.nextNode, count)

  def get(self, i):
    '''Returns the data at index i (counting from 0).  You may assume i is a
    valid index'''
    return self.__get(i, self.head, 0)

  def __get(self, i , node, Index):
    if i == Index:
      return node.data
    Index += 1
    return self.__get(i, node.nextNode, Index)

  def addBefore(self, findElement, addElement):
    '''Adds addElement to the list, so that it appears right before the first
    appearance of findElement in the list.  If findElement is not in the list,
    addElement should be added to the end of the list.'''
    self.__addBefore(findElement, addElement, self.head)
    return 0
    
  def __addBefore(self, findElement, addElement, node):
    if node.nextNode == None:
      newNode = Node
      node.nextNode = newNode
      self.tail = newNode
      return
    if node.nextNode.data == findElement:
      newNode = Node(addElement)
      newNode.nextNode = node.nextNode
      node.nextNode = newNode
      return
    self.__addBefore(findElement, addElement, node.nextNode)