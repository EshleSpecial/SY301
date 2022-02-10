import sys

#DO NOT MODIFY THE NODE OR STACK CLASS
class Node:
    def __init__(self, val):
        self.data = val
        self.nextNode = None

class Stack:
    def __init__(self):
        self.head = None

    #Returns True if the stack is empty
    def isEmpty(self):
        return self.head == None

    def push(self, val):
        newNode = Node(val)
        newNode.nextNode = self.head
        self.head = newNode

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty, cannot pop")
        val = self.head.data
        self.head = self.head.nextNode
        return val

    def peek(self):
        return self.head.data

#Your code goes here
def main():
    myStack = Stack()
    lessStack = Stack()
    with open(sys.argv[1]) as someHandle:
        for lineOfText in someHandle:
            if 'ssh' in lineOfText:
                myStack.push(lineOfText[4:-1])
            if "less" in lineOfText:
                while myStack != None:
                    p = myStack.pop()
                    lessStack.push(p)
                    while lessStack != None:
                        po = lessStack.pop()
                        myStack.push(po)
                        print(myStack)
            if "exit" in lineOfText:
                myStack.pop()   

if __name__ == "__main__":
    main()