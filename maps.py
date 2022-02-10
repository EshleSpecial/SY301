#MIDN McKenzie Eshleman
#221938
#LAB 7

import bisect

class KVPair:
   
    def __init__(self,key,value):
        self.key = key
        self.value = value
    
    def __lt__(self,other):
        if self.key < other.key:
            return True
        else:
            return False
    
    def __le__(self,other):
        if self.key <= other.key:
            return True
        else:
            return False
    def __gt__(self,other):
        if self.key > other.key:
            return True
        else:
            return False
    def __ge__(self,other):
        if self.key >= other.key:
            return True
        else:
            return False
    def __eq__(self,other):
        if self.key == other.key:
            return True
        else:
            return False
    def __ne__(self,other):
        if self.key != other.key:
            return True
        else:
            return False


class SortedArrayMap:

#init function that initializes Map with empty array
    def __init__(self):
        self.arrayMap = []

#insert key value pairs
    def __setitem__(self,key,value):
        pair = KVPair(key,value)
        bisect.insort_left(self.arrayMap, pair)
#given a key get the value 

    def __getitem__(self, k):
        for i in range(len(self.arrayMap)):
            if (self.arrayMap[i].key == k):
                return self.arrayMap[i].value
    
    def __contains__(self, k):
        for i in range(len(self.arrayMap)):
            if(self.arrayMap[i].key == k):
                return True
    
    def printall(self):
        for i in range(len(self.arrayMap)):
            print(str(self.arrayMap[i].key) + ", " + str(self.arrayMap[i].value))