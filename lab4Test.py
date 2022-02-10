from linkedlist import *

def printInOrder():
    ll = LinkedList()
    for i in range(10, 0, -1):
        ll.add2Front(i)

    ll.printInOrder()

def printInReverseOrder():
    ll= LinkedList()
    for i in range(10, 0, -1):
        ll.add2Front(i)
    ll.printInReverseOrder()

def isIn():
    ll = LinkedList()
    ll.add2Front(5)
    ll.add2Front(4)
    ll.add2Front(1)
    print(ll.isIn(5))
    print(ll.isIn(1))
    print(ll.isIn(3))

def isInTimes():
    ll = LinkedList()
    ll.add2Front(5)
    ll.add2Front(4)
    ll.add2Front(1)
    ll.add2Front(1)
    ll.add2Front(1)
    ll.add2Front(4)

    print(ll.isInTimes(1))
    print(ll.isInTimes(4))
    print(ll.isInTimes(0))

def get():
    ll = LinkedList()
    ll.add2Front(5)
    ll.add2Front(4)
    ll.add2Front(1)
    ll.add2Front(1)
    ll.add2Front(1)
    ll.add2Front(4)

    print(ll.get(0))
    print(ll.get(3))

def addBefore():
    ll = LinkedList()
    ll.add2Front(5)
    ll.add2Front(3)
    ll.add2Front(1)
    ll.add2Front(8)
    ll.addBefore(3, 4)
    ll.addBefore(5, 9)
    ll.printInOrder()

def remove():
    ll = LinkedList()
    ll.add2Front(5)
    ll.add2Front(3)
    ll.add2Front(1)
    ll.add2Front(8)
    ll.remove(2)
    ll.printInOrder()
    print()
    ll.remove(1)
    ll.printInOrder()