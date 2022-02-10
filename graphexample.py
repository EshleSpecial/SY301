#output dictionary, where keys = node ID, val = back pointer
def shortestPath(start):
    back = {}
    toVisit = Queue()
    toVisit.enter(start)
    while not toVisit.empty():
        cur = toVisit.dequeue()
        for i in cur return.Adjacent():
            if not i in back:
                toVisit.
