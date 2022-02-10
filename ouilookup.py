import sys


from maps import KVPair

def read():
    ouis = []
    f = open('ouis.txt', 'rb')
    line = f.readlines()
    for i in line:
            info = i.split()
            address = info[0] #This is the mac address info
            name = info[1] #This is the first line name of Mac Address
            ouis = ouis.append((address, name))
            print(ouis)
            f.close()
read()



















#print("NovatelW Unknown\nCisco Broadcast\nCisco Unknown\nNovatelW Unknown\nUnknown Broadcast\nNovatelW Unknown\nCisco Unknown\nCisco Unknown\nCisco Unknown\nNovatelW Unknown\nUnknown Broadcast\nUnknown Unknown\nUnknown Broadcast\nUnknown Broadcast\nCisco Unknown\nCisco Unknown\nCisco Unknown\nCisco Unknown\nUnknown Broadcast\nUnknown Broadcast\nUnknown Broadcast\nUnknown Broadcast\nUnknown Broadcast\nCisco Broadcast\nCisco Broadcast\nCisco Unknown\nCisco Unknown\nUnknown Unknown\nCiscoMer Broadcast\nNovatelW Unknown\nCisco Unknown\nUnknown Broadcast\nCisco Broadcast\nUnknown Broadcast\nCisco Unknown\nNovatelW Unknown\nCisco Unknown\nUnknown Broadcast\nCisco Unknown\nUnknown Unknown")
        
    
