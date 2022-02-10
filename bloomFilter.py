#MIDN McKenzie Eshleman
#221938
#Lab 8 Bloom Filter

import math
import hashlib

class BloomFilter:

    def __init__(self,capacity):
        self.list = [False] * capacity

    def add(self,key):
        for i in range(1,3):
            hashOut = self.hashSlingingSlasher(i,key)
            index = hashOut % len(self.list)
            self.list[index] = True

    def __contains__(self,key):
        for i in range(1,3):
            hashOut = self.hashSlingingSlasher(i,key)
            index = hashOut % len(self.list)
            if(self.list[index] == False):
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
