import hashlib,string,sys,random,os

def usage():
  print('Must run with four arguments, one for the file from which to read')
  print('passwords and counts, one for the number of elements in the table,')
  print('one with the filename for the hashed table, and one for the filename')
  print('for the plaintext solution.')
  print('Ex: python3 pwPageGenerator.py shortrockyouwithcount.txt 5000 outHashes.txt outAnswers.txt')

numChoices=0
outFile=''
outAns=''
inFile=''
if len(sys.argv)<5:
  usage()
  exit()
try:
  inFile=sys.argv[1]
  numChoices=int(sys.argv[2])
  outFile=sys.argv[3]
  outAns=sys.argv[4]
except:
  usage()
  exit()
exclude = set(string.punctuation)
usernames=set()
with open('american-english','r') as uns:
  for word in uns:
    un=''.join(ch for ch in word.rstrip() if ch not in exclude)
    usernames.add(un.lower())
passwords=[]
with open(inFile,'r') as pws:
  for line in pws:
    lineArr = line.rstrip().split()
    if len(lineArr) < 2:
      continue
    c = int(lineArr[0])
    for i in range(c):
      passwords.append(lineArr[1])


usernames=random.sample(usernames,numChoices)
salt = os.urandom(16)
with open(outFile,'w') as hashes, open(outAns,'w') as answers:
  hashes.write("salt\t" + salt.hex() + "\n")
  for i in range(len(usernames)):
    m=hashlib.sha256()
    m.update(salt)

    un = usernames[i]
    pw=random.choice(passwords)

    leakageLen = random.choice([1,1,1,2,2,3])
    leakage = pw[:leakageLen]
    
    answers.write(un+'\t'+pw+'\n')
    pw=pw.encode()
    m.update(pw)
    hashes.write(un+'\t'+m.hexdigest()+"\t" + leakage + '\n')
