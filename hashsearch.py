import hashlib, bisect



#This function hashes a password with a salt to return its hash
#Arguments:
#   pw - String containing the password to be hashes
#   salt - bytes object containing the salt
def hashPass(pw, salt):
    h = hashlib.sha256()
    h.update(salt)
    h.update(pw.encode())
    return h.digest()
#STEP 1
class HashSearch:
    #Arguments:
    #   passwords - list of passwords strings, in descending order of frequency (most popular password at index 0)
    #   counts - counts of how many times each password occurs, indices correspond to the password list
    #   salt - the salt used to calculate hashes
    def __init__(self, passwords, counts, salt):
        self.salt = salt
        #Your code here
        passwords.sort()
        self.array = passwords
        self.counts = counts

    #Arguments:
    #   pwHash - hash of the password that you are trying to break, in hex (a string)
    #   leakage - first few characters of the password leaked by the weak password security policy, 1-3 characters    
    #Return - The password corresponding to this hash
    def crack(self, pwHash, leakage):
        #binary search of the array and leakage
        l = 0
        r = len(self.array)
        while(l < r):
            m = l + ((r-l)//2) #middle
            res = (leakage == self.array[m])

            if (self.array[m] < leakage):
                l = m + 1
            else:
                r = m - 1
        while l < len(self.array):
            hashVal =hashPass(self.array[l], self.salt).hex()
            if hashVal == pwHash:
                return self.array[l]
            l += 1
#STEP 2
class HashSearchTable:

    def __init__(self, passwords, counts, salt):
    #1) Loop through all passwords Hash each one using hashPass, then hash again
    #using hash function, like in bloom filter
    # will give you an index to put this (hash,password) pair.

        self.salt = salt
        self.hashTable = [None] * (len(passwords) * 2)
    
        passwords.sort()
        for i in passwords:
            hashValue = hashPass(i, self.salt).hex()
            index = hash(hashValue) % len(self.hashTable)
            if self.hashTable[index] == None:
                self.hashTable[index] = []
            self.hashTable[index].append((hashValue,i))

    def crack(self, pwHash):
    #1) Look up pwHash in your hash table, return password plaintext
        index = hash(pwHash) % len(self.hashTable)
        for i in self.hashTable[index]:
            if pwHash == i:
                return(self.hashTable[i])
class HashSearchPlus:
    def __init__(self, salt, passwords,counts):
        self.dict = {}
        self.salt = salt
        self.counts = counts
        passwords.sort()
        self.dict = {passwords}

    def crack(self):
        pass