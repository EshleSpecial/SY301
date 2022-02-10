
import sys
from collections import deque
import random

class Vertex:

    def __init__(self, vertexName):
        self.name = vertexName 
        self.adjacentDict = {} 
        self.adjacentList = []  

    def addNeighbors(self, neighbors):
        neighborsName = neighbors.name
        self.adjacentDict[neighborsName] = neighbors
        self.adjacentList.append(neighbors)

class Graph:
    
    def __init__(self,filename):
        self.verticesDict = {} 
        self.connection = True
        self.name = "" 

    def __len__(self):
        return len(self.verticesDict.keys())

    def dotBuilder(self, filename):
        try:
            with open(filename, 'r') as dotFile:
                fileLines = dotFile.readlines()
        except:
            print("ERROR: Invalid file ")
            exit()
        for line in fileLines:
            if line.startswith("graph") or line.startswith("digraph"): 
                bannanaSplits = line.split(" ")
                self.name = bannanaSplits[1]
                continue 
            elif line.startswith("}"):
                break
            elif line.startswith("graph") == False and line.startswith("digraph") and line.startswith("}"):
                print("ERROR: Invalid Dot File Format")
                exit()
            if "->" in line: 
                bannanaSplits = line.split(" -> ")
                directOrUndirect = " -> "
                self.connection = True
            else:
                bannanaSplits = line.split(" -- ")
                directOrUndirect = " -- "
                self.connection = False
            self.connect = directOrUndirect
        
            firstName = (bannanaSplits[0].strip()) 
            secondName = (bannanaSplits[1].strip().strip(';'))
            if firstName not in self.verticesDict: 
                self.addVertex(firstName) 
            if secondName not in self.verticesDict: 
                self.addVertex(secondName) 
            self.addEdge(firstName, secondName)

    def addVertex(self, vertexName):
        vertex = Vertex(vertexName)
        self.verticesDict[vertexName] = vertex
        return vertex

    def addEdge(self, vertex1, vertext2):
        vert1 = (self.verticesDict[vertex1])
        vert2 = (self.verticesDict[vertext2] )
        vert1.addNeighbors(vert2)
        if self.connection is False:
            vert2.addNeighbors(vert1)
    
    def hopper(self, name, hops):
        root = None
        for key in self.verticesDict: 
            if int(self.verticesDict[key].name) == int(name): 
                root = self.verticesDict[key]
        startAdjacent = root
        if root == None:
            print("['0']\n")
        steps = -1
        vertexIDDict = dict()
        queue = deque()
        queue.append(startAdjacent)
        while steps < hops:
            neighbors = []
            while len(queue) > 0:
                currAdjacent = queue.popleft()
                current_vertexName = currAdjacent.name
                if current_vertexName not in vertexIDDict: 
                    vertexIDDict[current_vertexName] = steps + 1
                else:
                    continue
                for vert in currAdjacent.adjacentList:
                    neighbors.append(vert)
            for neighbor in neighbors:
                queue.append(neighbor)
            steps += 1
        rtList =[]
        for key in vertexIDDict:
            rtList.append(key)
        return rtList

    def canSurveil(self, suspect, target, hops):
        suspectHopsList = self.hopper(suspect, hops)
        if str(target) in suspectHopsList:
            return True
        else:
            return False

    def percentage(self, suspect, hops):
        try:
            suspectHopsList = self.hopper(suspect, hops)
        except TypeError:
            print("hops must be an int")
            exit()
        rtList=[]
        percent = float(len(suspectHopsList) / len(self.graph)) * 100
        return percent

    def likelyPercentage(self, hops):
        deviation = 0
        count = 0
        randomCount =0 
        runningPercent = 0
        traversed= []
        randomKey = random.randint(0, len(self.graph) - 1)
        for key in self.graph.verticesDict:
            if randomCount <= randomKey:
                randomCount += 1
                continue
            if count >= 30:
                break
            if key not in traversed:
                traversed.append(key)
            else:
                continue
            deviation = self.percentage(key, hops)
            if count > 0:
                if (((runningPercent / count) - deviation) >= 1) or (((runningPercent / count) - deviation) <= -1):
                    continue
                else:
                    runningPercent += deviation
                    count +=1
            else:
                runningPercent += deviation
                count +=1
        return float(runningPercent / count)