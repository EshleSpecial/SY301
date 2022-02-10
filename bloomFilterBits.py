#MIDN McKenzie Eshleman
#221938
#Lab 8 Bloom Filter

import math
import hashlib

class BloomFilter:

    def __init__(self,capacity):
        self.int = 0 
        self.maxCapacity = capacity
        return

    def add(self,key):
        for i in range(1,3):
            hashOut = self.hashSlingingSlasher(i,key)
            index = hashOut % self.maxCapacity
            shift = 1 << index
            self.int = self.int | shift

    def __contains__(self,key):
        for i in range(1,3):
            hashOut = self.hashSlingingSlasher(i,key)
            index = hashOut % self.maxCapacity
            shift = 1 << index 
            if not(self.int & shift):
                return False
        return True

    def hashSlingingSlasher(self, hashType, inputValues):
        if (hashType == 1):
            hashObject = hashlib.md5()
        if (hashType == 2):
            hashObject = hashlib.sha256()
        if (hashType == 3):
            hashObject = hashlib.sha512()
        bytestr = inputValues.encode()
        hashObject.update(bytestr)
        hexSTR = hashObject.hexdigest()
        out = int(hexSTR, 16)
        return(out)  
