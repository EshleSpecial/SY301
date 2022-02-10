from linkedlist import *

def nodeConstructor():
    n = Node(5)
    if n.data == 5 and n.nextNode == None:
        return True
    return False

def llConstructor():
    ll = LinkedList()
    if ll.head == None and ll.tail == None:
        return True
    return False

def llAdd2Front():
    ll = LinkedList()
    print("Adding 5")
    ll.add2Front(5)
    print("Adding 10")
    ll.add2Front(10)
    print("Head is " + str(ll.head.data) + " and nextNode is " + str(ll.head.nextNode.data))
    return False

def llAdd2FrontSetsTail():
    ll = LinkedList()
    ll.add2Front(5)
    ll.add2Front(10)
    print("Adding 5 and 10")
    print("Tail is " + str(ll.tail.data))
    return False

def llAdd2Back():
    ll = LinkedList()
    print("Adding 10 to back")
    ll.add2Back(10)
    print("Adding 5 to back")
    ll.add2Back(5)
    print("Tail is " + str(ll.tail.data))
    return False

def llAdd2BackSetsHead():
    ll = LinkedList()
    print("Adding 10 to back")
    ll.add2Back(10)
    print("Adding 5 to back")
    ll.add2Back(5)
    print("Head is " + str(ll.head.data))
    return False

def llString():
    ll = LinkedList()
    print("Adding to front 5, 4, 3")
    ll.add2Front(5)
    ll.add2Front(4)
    ll.add2Front(3)
    s = str(ll)
    print("String returned: " + s.strip())
    return False

def llIsIn():
    ll = LinkedList()
    print("Adding to front 5, 10 1")
    ll.add2Front(5)
    ll.add2Front(10)
    ll.add2Front(1)
    print("isIn(5): " + str(ll.isIn(5)))
    print("isIn(4): " + str(ll.isIn(4)))
    return False

def llAddInOrderEmpty():
    ll = LinkedList()
    print("addInOrder(5) on empty list")
    ll.addInOrder(5)
    print("Head: " + str(ll.head.data))
    print("Tail: " + str(ll.tail.data))

def llAddInOrder():
    ll = LinkedList()
    print("Adding 5, 3, 1 to the front")
    
    ll.add2Front(5)
    ll.add2Front(3)
    ll.add2Front(1)

    print("Adding in order 0, 8, 4")
    ll.addInOrder(0)
    ll.addInOrder(8)
    ll.addInOrder(4)
    
    print("Result: " + str(ll))
