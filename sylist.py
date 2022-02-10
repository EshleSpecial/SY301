#Creates a new array of the given size
def malloc(size):
  return [None]*size

class SYList:
  #Initialize an SYList with the given capacity, defaults to 0
  def __init__(self, capacity=0):
    self.array = malloc(capacity)

    #Stores the number of elements in the list
    self.length = 0

    #Stores the capacity of the list
    self.capacity = capacity


  #Allows users to call len() on SYList objects
  def __len__(self):
    return self.length

  #getitem and setitem allow index operator [] to work on SYList objects
  def __getitem__(self, index):
    if index >= self.length or index < 0:
      raise IndexError("Index out of range")
    return self.array[index]

  def __setitem__(self, index, value):
    if index >= self.length or index < 0:
      raise IndexError("Index out of range")
    self.array[index] = value

  #Should return the list as a string, including only the elements actually in the list (not the extra slots that are yet to be filled)
  #The output should be identical to python's output when printing a normal list, i.e. "[1, 2, 3, 4]"
  def __str__(self):
      return str(self.array[:self.length])


  #Should add one new item (value) to the end of the list, increasing the length and capacity by 1
  def append(self, value):
    #STEP 1: add a new element to the list
    self.array = self.array + [value]
    #Step 2 if there are no remaining capacity in the list, make a new array using malloc function
    if self.capacity == self.length:
        newArray = malloc(self.capacity + 1)
        for i in range(self.capacity):
            newArray[i] = self.array[i]
#STEP 3: When making a new array it should copy to self.array
    self.array = newArray
      


  #Should add one new item (value) to the end of the list increasing the length by 1. If the capacity is full, it should increase the array capacity by 5.
  def append5(self, value):
    self.array = self.array + [value]
    if self.capacity == self.length:
        newArray = malloc(self.capacity + 5)
        for i in range(self.capacity):
            newArray[i] = self.array[i]
    self.array = newArray

  #Should add one new item (value) to the end of the list increasing the length by 1.  If the capacity is full, it should double the capacity.
  def appendDouble(self, value):
    self.array = self.array + [value]
    if(self.capacity == 0):
        newArray = malloc(self.capacity + 1)
        for i in range(self.capacity):
            newArray[i] = self.array[i]
    self.array = newArray

    if self.capacity == self.length:
        newArray = malloc(self.capacity * 2)
        for i in range(self.capacity):
            newArray[i] = self.array[i]
    self.array = newArray
