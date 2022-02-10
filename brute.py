#!/usr/bin/python3
from datetime import datetime
import sys

def usage():
  print('This program is to be run with three arguments.  The first is the filename of your dictionary ')
  print('file, such as shortrockyouwithcount.txt or rockyouwithcount.txt.  The second is the file you are')
  print('trying to crack, which was likely created by pwPageGenerator.py, and contains usernames')
  print('and the hashes of passwords.  The third is the name of the class to use for cracking (i.e. HashSearch).')
  print('Cracked passwords will be printed to the screen and also written to the file cracked.txt.')
  print('EXAMPLE:')
  print('python3 brute.py shortrockyouwithcount.txt outTable.txt HashSearch')

if len(sys.argv) != 4:
  usage()
  exit()
passwords=[]
counts = []
hashes = []
try:
  with open(sys.argv[1],'r') as f:
    for line in f:
      linesplits = line.strip().split()
      if len(linesplits) != 2:
        continue
      passwords.append(linesplits[1])
      counts.append(int(linesplits[0]))
  with open(sys.argv[2],'r') as f:
    saltline = f.readline()
    if not "salt" in saltline:
      print("Error: hash file does not contain a salt")
      exit()
    salt = bytes.fromhex(saltline.split()[1])
    for line in f:
      linesplits = line.strip().split()
      hashes.append((linesplits[0],linesplits[1],linesplits[2]))
    
    
except:
  usage()
  exit()

start=datetime.now()
print("Initializing data structure")
m = __import__("hashsearch")
C = getattr(m, sys.argv[3])
s = C(passwords,counts,salt)

answerStrings = []
print("Begin cracking")
for (usr,hsh,leak) in hashes:
  print("Cracking " + hsh + " with hint " + leak)
  pw = s.crack(hsh,leak)
  if pw != None:
    answerStrings.append(usr + "\t" + pw)
  else:
    answerStrings.append(usr + '\t' + 'NOTFOUND')
stop=datetime.now()
print("Answers:")
with open("cracked.txt", "w") as f:
  for answers in answerStrings:
    print(answers)
    f.write(answers + "\n")
print("Runtime: ",stop-start)
