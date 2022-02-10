class PCAP:

    def __init__(self,filename):
        self.file = filename
        self.entries = []
        with open(filename, 'r') as log:
            for line in log:
                if (line != "\n"):
                    newEntry = entry(line)
                    self.entries.append(newEntry)

    def packetsBySource(self): 
        tupList = []
        for i in range(len(self.entries)):
            source = self.entries[i].source
            added = False
            for j in range(len(tupList)): 
                if tupList[j][0] == source:
                    currentValue = tupList[j][1]
                    newValue = int(currentValue) + 1
                    newTup = (source, int(newValue))
                    tupList[j] = newTup
                    added = True
                    break
            if added == False:
                newTup = (source, int(1))
                tupList.append(newTup)
        sortedList = str(Sort(tupList, 1))
        return sortedList


    def bytesBySource(self):
        tupList = []
        for i in range(len(self.entries)):
            source = self.entries[i].source
            size   = self.entries[i].bytes
            added = False
            for j in range(len(tupList)): 
                if tupList[j][0] == source: 

                    currentValue = tupList[j][1]
                    newValue = int(currentValue) + int(size)
                    newTup = (source, int(newValue))
                    tupList[j] = newTup
                    added = True
                    break

            if added == False: 
                newTup = (source, int(size)) 
                tupList.append(newTup)
        sortedList = str(Sort(tupList, 1))
        return sortedList


    def packetsByConnections(self):
        
        tupList = []
        for i in range(len(self.entries)):
            protocol = self.entries[i].protocol
            added = False
            for j in range(len(tupList)): 
                if tupList[j][0] == protocol: 

                    currentValue = tupList[j][1]
                    newValue = int(currentValue) + 1
                    newTup = (protocol, int(newValue))
                    tupList[j] = newTup
                    added = True
                    break

            if added == False: 
                newTup = (protocol, 1) 
                tupList.append(newTup) 
        sortedList = str(Sort(tupList, 1))
        return sortedList

    def bytesByProtocols(self): 

        tupList = []
        for i in range(len(self.entries)):
            protocol = self.entries[i].protocol
            size     = self.entries[i].bytes
            added = False
            for j in range(len(tupList)): 
                if tupList[j][0] == protocol: 

                    currentValue = tupList[j][1]
                    newValue = int(currentValue) + int(size)
                    newTup = (protocol, int(newValue))
                    tupList[j] = newTup
                    added = True
                    break

            if added == False:
                newTup = (protocol, int(size))
                tupList.append(newTup) 
        sortedList = str(Sort(tupList, 1))
        return sortedList

    def bytesByConnections(self):

        tupList = []
        for i in range(len(self.entries)):
            source = self.entries[i].source
            destination = self.entries[i].destination
            size = self.entries[i].bytes
            added = False
            for j in range(len(tupList)): 
                if (tupList[j][0] == source) and (tupList[j][1] == destination): 
                    currentValue = tupList[j][2]
                    newValue = int(currentValue) + int(size)
                    newTup = (source, destination, int(newValue))
                    tupList[j] = newTup
                    added = True
                    break

            if added == False:
                newTup = (source, destination, int(size))
                tupList.append(newTup) 
        sortedList = str(Sort(tupList, 1))
        return sortedList

def Sort(data, INDX):
    length = len(data)
    if length <= 1:
        return data
    left = Sort(data[:int(length/2)], INDX)
    right = Sort(data[:int(length/2):], INDX)
    return Merger(left, right, INDX)

def Merger(left, right, INDX):
    sortArray = []
    i, j = 0, 0
    while True:
        if i == len(left) and j == len(right):
            break
        elif j == len(right):
            sortArray.append(left[i])
            i += 1
        elif i == len(left):
            sortArray.append(right[j])
            j += 1
        elif int(left[i][INDX]) <= int(right[j][INDX]):
            sortArray.append(left[i])
            i += 1
        else:
            sortArray.append(right[j])
            j += 1
    return sortArray

class entry:

    def __init__(self, string):
        divided = string.split(",")
        self.source = divided[2].replace('"', '')
        self.destination = divided[3].replace('"', '')
        self.protocol = divided[4].replace('"', '')
        self.bytes = divided[5].replace('"', '')