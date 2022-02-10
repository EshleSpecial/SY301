#MIDN ESHLEMAN
#221938

import sys
from bst import Node
from bst import TreeSet

Tree = TreeSet()

def badWords(cmdArgv=None):
    with open("badwords.txt", 'r') as badWordsFile:
        while(1):
            word = badWordsFile.readline()
            if (word = ""):
                break
            Tree.insert(word.strip())
    return

def searchword(cmdArgv=None):
    with open(sys.argv[1], 'r') as txtfile:
        words = []
        for line in txtfile:
            for word in line.split():
                words.append(word)
    counter = 0
    for i in range(len(words)):
        phrase = words[i]
        phrase = normalstrings(phrase)
        for five in range(5):
            index = (i + five)
            if(index >= len(words)):
                index = (len(words)-1)
            if(five != 0):
                stripWord = words[index]
                stripWord = normalstrings(stripWord)
                phrase = str(phrase.strip() + " " + stripWord)
            if phrase in Tree:
                print(phrase)
                counter += 1
                break
    print("Count: " + str(counter))
    return

def normalstrings(badstrings):
    sansWhitespace = badstrings.strip()
    strippedstrings = ""
    for char in sansWhitespace:
        if char.isalnum():
            strippedstrings += char
    #LOWERCASE
    lowerStr = strippedstrings.lower()
    normalstrings = lowerStr
    return normalstrings

def main(cmdArgv=None):
    try:
        badWords()
        searchword()
    except FileNotFoundError:
        print("INVALID FILE")
        exit()
    return

if __name__ == "__main__":
    main()