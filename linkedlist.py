#Midn McKenzie Eshleman
#221938
#SY301 
#25 AUG 20

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add2Front(self, data):
        newNode = Node(data)
        #Data input as an argument should be put in a new node
        #calling function myLL.add2Front(4) should output 4, 1, 3, 5
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            tempNode = self.head
            self.head = newNode
            newNode.nextNode = tempNode
        return 0

    def add2Back(self, data):
        #data input as an argument should be out inside a new node
        #Then it should be stuck on the back of the Linked List
        #calling function myLL.add2Back(4) should output 1,3,5,4
        newNode = Node(data)
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.nextNode = newNode
            self.tail = newNode
        return 0


    def iterator(self):
        current = self.head
        while current != None:
      #Do something with cur, i.e. print it or add its value to a string
            return current
        current = current.nextNode

    def __str__(self):
        #return all the data within the Linked List as a string
        #calling this function should output 1 3 5
        #if the list is empty then it should be a empty string
        #return "{}".format(self.head)
        current = self.head
        if current == None: #checks for empty list
            print(" ")
            return 1
        while (current.nextNode != None):
            print(current.data)
            current = current.nextNode
        print(current.data)


    def isIn(self, data):
        #Calling myLL.isIn(some number) should return true if the number 
        #is in the node, false if it is not
        current = self.head
        tempNode = Node(data)
        while current.nextNode != None:
            if current.data == tempNode.data:
                return True
            current = current.nextNode
        return False


    def addInOrder (self, data):
        #takes data and adds it in a appropriate place
        current = self.head
        before = self.head
        tempNode = Node(data)
        if(self.head.data > tempNode.data):
            tempNode.nextNode = self.head
            self.head = tempNode
            return 1
        if(self.tail.data < tempNode.data):
            self.tail.nextNode = tempNode
            self.tail = tempNode
            return 1
        while current.data < tempNode.data:
            before = current
            current = current.nextNode
        
        tempNode.nextNode = current
        before.nextNode = tempNode

        return 0
