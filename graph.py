class Vertex:

    def __init__(self,vertex,adjList, connect=""):
        self.name = vertex
        self.adjacentList = []
        self.connect = connect

    def addNeighbors(self,Neighbors):
        self.adjacentList.append(Neighbors)

class Graph:

    def __init__(self, filename=None):
        self.filename = filename
        self.graphName = ""
        self.verticesDict = {}
        self.connect = ""
    
    def buildFromDot(self,filename):
        try:
            with open(filename, 'r') as dotFile:
                filelines = dotFile.readlines()
        except:
            print("ERROR: INVALID FILE ")
            exit()
        for line in filelines:
            if line.startswith("graph") or line.startswith("digraph") and line.startswith("}"):
                bannanasplits = line.split(" ")
                self.name = bannanasplits[0] + ": " + bannanasplits[1]
                continue
            elif line.startswith("}"):
                break
            elif line.startswith("graph") == False and line.startswith("digraph") and line.startswith("}"):
                print("ERROR: Invalid Dot File Format")
                exit()
            if "->" in line:
                bannanasplits = line.split(" -> ")
                directorUndirect = " -> "
            else:
                bannanasplits = line.split(" -- ")
                directorUndirect = " -- "
            self.connect = directorUndirect
            firstName = bannanasplits[0].strip()
            secondName = bannanasplits[1].strip().strip(';')
            if firstName not in self.verticesDict:
                self.verticesDict[firstName] = Vertex(firstName, directorUndirect)
            if secondName not in self.verticesDict:
                self.verticesDict[secondName] = Vertex(secondName, directorUndirect)
            if directorUndirect == " -> ":
                self.verticesDict[secondName] = Vertex(secondName, directorUndirect) 
                self.verticesDict[firstName].addNeighbors(self.verticesDict[secondName])
                continue
            self.verticesDict[firstName].addNeighbors(self.verticesDict[secondName])
            self.verticesDict[secondName].addNeighbors(self.verticesDict[firstName])
    
    def returnAdjacent(self,vertex):
        if vertex not in self.verticesDict:
            print("Vertext: " + vertex + "Not found")
            return None
        for i in self.verticesDict:
            if self.verticesDict[i].name == vertex and self.connect != " -> ":
                print("Adjacent list for vertex: " + str(self.verticesDict[i].name))
                rtList = []
                for j in range(len(self.verticesDict[i].adjacentList)):
                    rtList.append(self.verticesDict[i].adjacentList[j].name.strip(" -- "))
                return rtList
            elif self.verticesDict[i].name == vertex:
                print("Adjacent list for vertex: " + str(self.verticesDict[i].name))
                rtList = []
                for j in range(len(self.verticesDict[i].adjacentList)):
                    if not self.isAdjacent(i, self.verticesDict[i].adjacentList[j].name):
                        continue
                    rtList.append(self.verticesDict[i].adjacentList[j].name)
                return rtList
    
    def isAdjacent(self,vertexA, vertexB):
        for i in self.verticesDict:
            if self.verticesDict[i].name == vertexA and self.verticesDict[i].connect.strip() == "--":
                for j in range(len(self.verticesDict[i].adjacentList)):
                    if self.verticesDict[i].adjacentList[j].name.strip(" -- ") == vertexB:
                        return True
            
            elif self.verticesDict[i].name == vertexA:
                for j in range(len(self.verticesDict[i].adjacentList)):
                    if self.verticesDict[i].adjacentList[j].name == vertexB:
                        return True
        return False


    def __str__(self):
        List = [] 
        st = "\ngraph" + self.name + " {\n\n\t"

        for i in self.verticesDict:
            for j in range(len(self.verticesDict[i].adjacentList)):
                node = self.verticesDict[i].adjacentList[j].name
                edge = str(self.verticesDict[i].name) + " " + self.verticesDict[i].connect + " " + str(node)
                otheredge = str(node) + " " + self.verticesDict[i].connect + " " + str(self.verticesDict[i].name)
                if otheredge not in List:
                    List.append(edge)
        for i in range(len(List)):
            rtList = List[i].split()
            if len(rtList) != 3:
                wait = rtList[1]
                rtList[1] = self.connect.strip()
                rtList.append(wait)
            firstName = rtList[0]
            directOrUndirect = rtList[1]
            secondName = rtList[2]
            rtList += firstName + " " + directOrUndirect + " " + secondName + ";\n\t"
        st += "\n}"
        return st